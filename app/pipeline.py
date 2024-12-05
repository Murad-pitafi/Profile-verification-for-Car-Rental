# pipeline.py
import re

def process_file(file_path):
    with open(file_path, 'r',  encoding='utf-8') as f:
        data = f.read()

    # Step 1: Extract username
    username_match = re.search(r"([^\n]+)\s+(?:2nd degree|3rd degree)", data)
    username = username_match.group(1).strip() if username_match else "Not available"

    # Step 2: Extract number of connections
    connections_match = re.search(r"(\d+\+?)\s+connections", data)
    connections = connections_match.group(1) if connections_match else "Not available"

    # Step 3: Extract experience and calculate total years and months
    experience_pattern = r"Experience(.*?)Education"
    experience_section = re.search(experience_pattern, data, re.DOTALL)
    experience_section = experience_section.group(1).strip() if experience_section else ""

    duration_pattern = r"(\d+)\s+yrs(?:\s+(\d+)\s+mos)?"
    matches = re.findall(duration_pattern, experience_section)

    # Remove duplicates by converting to a set
    unique_matches = list(set(matches))

    # Calculate total years and months
    total_years = 0
    total_months = 0
    for match in unique_matches:
        years = int(match[0]) if match[0] else 0
        months = int(match[1]) if match[1] else 0
        total_years += years
        total_months += months

    # Convert months to years if needed
    total_years += total_months // 12
    total_months = total_months % 12

    # Step 4: Extract education
    education_pattern = r"Education(.*?)(?:Licenses & certifications|Projects|$)"
    education = re.search(education_pattern, data, re.DOTALL)
    education = education.group(1).strip() if education else "Not available"

    # Step 5: Extract the highest-priority degree using broader matching
    degree_patterns = {
        "PhD": r"ph\.?d|doctorate|doctoral",
        "MS": r"m\.?s|master|masters|m\.sc",
        "BS": r"b\.?s|b\.sc"
    }

    def extract_highest_priority_degree(data, degree_patterns):
        for degree, pattern in degree_patterns.items():
            if re.search(pattern, data, re.IGNORECASE):
                return degree
        return "None"

    highest_degree = extract_highest_priority_degree(education, degree_patterns)

    # Step 6: Extract recent post timing
    post_pattern = r'(\d+)(mo|d|yr)'
    post_match = re.findall(post_pattern, data)
    if post_match:
        number, unit = post_match[0]
        if unit == 'mo':
            recent_post = f"{number} months"
        elif unit == 'yr':
            recent_post = f"{number} years"
        elif unit == 'd':
            recent_post = f"{number} days"
        else:
            recent_post = "Not available"
    else:
        recent_post = "Not available"

    # Step 7: Extract reactions, comments, and repost counts
    reaction_regex = r'like\w*\s*(\d+)\s*'
    comments_regex = r'(\d+)\s*comments'
    reposts_regex = r'(\d+)\s*reposts'
    reaction_match = re.search(reaction_regex, data)
    comments_match = re.search(comments_regex, data)
    reposts_match = re.search(reposts_regex, data)
    reactions = reaction_match.group(1) if reaction_match else "Not available"
    comments = comments_match.group(1) if comments_match else "Not available"
    reposts = reposts_match.group(1) if reposts_match else "Not available"

    # Compile all results into a dictionary, ensuring "Not available" values are replaced by 1
    results = {
        "Username": username if username != "Not available" else "Not available",  # Leave username as is
        "Education": highest_degree if highest_degree != "Not available" else "1",  # Set 1 for unavailable education
        "Experience (Years)": total_years if total_years > 0 else 1,  # Set 1 for unavailable experience years
        "Experience (Months)": total_months if total_months > 0 else 1,  # Set 1 for unavailable experience months
        "Connections": connections if connections != "Not available" else "1",  # Set 1 for unavailable connections
        "Recent Post": recent_post if recent_post != "Not available" else "1",  # Set 1 for unavailable recent post
        "Reactions on Recent Post": reactions if reactions != "Not available" else "1",  # Set 1 for unavailable reactions
        "Comments on Recent Post": comments if comments != "Not available" else "1",  # Set 1 for unavailable comments
        "Repost Count on Recent Post": reposts if reposts != "Not available" else "1",  # Set 1 for unavailable reposts
    }

    return results
