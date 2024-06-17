import pandas as pd

def extract_skills():
    # Load the job postings from the csv file
    df = pd.read_csv('job_postings.csv')
    
    # Extract and tally the skills
    skills_count = {}
    for summary in df['Summary']:
        if 'Python' in summary:
            skills_count['Python'] = skills_count.get('Python', 0) + 1
        if 'SQL' in summary: 
            skills_count['SQL'] = skills_count.get('SQL', 0) + 1
        
    print("Skills Tally:")
    for skill, count in skills_count.items():
        print(f"{skill}: {count}")
        
if __name__ == '__main__':
    extract_skills()