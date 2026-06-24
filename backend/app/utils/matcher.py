def calculate_match(job_skills, user_skills):

    matched = []

    missing = []

    for skill in job_skills:

        if skill in user_skills:

            matched.append(skill)

        else:

            missing.append(skill)

    score = 0

    if len(job_skills) > 0:

        score = round(

            len(matched)

            / len(job_skills)

            * 100

        )

    return {

        "match_score": score,

        "matched_skills": matched,

        "missing_skills": missing

    }