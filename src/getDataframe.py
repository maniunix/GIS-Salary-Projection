import pandas as pd

def getDataframe(jobs_desc):
    location = []
    job_role = []
    company = []
    salary = []
    salary_index = []
    for i in range(len(jobs_desc)):
        for j in range(len(jobs_desc[i])):
            try:
                for s, sal in enumerate(jobs_desc[i][j]):
                    if "000" in jobs_desc[i][j][s]:
                        salary.append(sal)
                        salary_index.append(s)
                        job_role.append(jobs_desc[i][j][0])
                        location.append(jobs_desc[i][j][2])
                        company.append(jobs_desc[i][j][1])
            except IndexError as ee:
                print(ee)

    return pd.DataFrame({"Location": location, "Company": company, "Salary": salary, "Job Role": job_role})