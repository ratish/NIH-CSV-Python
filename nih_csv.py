from numpy import empty
# import requests
import json
import csv


def checkEmptyValue(value):
    if value:
        return value
    return ""

# headers = {
#     'accept': 'application/json',
# }

# json_data = {
#     "criteria": {
#         "org_names": ["UNIVERSITY OF ARIZONA"]
#     },
#     "limit": 500
# }

# response = requests.post('https://api.reporter.nih.gov/v2/projects/search', headers=headers, json=json_data)

# data = json.loads(response.content)

# f = open("nih_csv_test.json", "w")
# f.write(json.dumps(data, indent=2))
# f.close()


f = open("nih_csv_test.json" ,"r")
data = json.loads(f.read())
f.close()

f_mt = open('nih_reporter_main_table.csv', 'w', encoding='UTF8', newline='\n')

writer_mt = csv.writer(f_mt)

header = ['appl_id',
'subproject_id',
'fiscal_year',
'project_num',
'project_serial_num',
'organization_org_name',
'organization_city',
'organization_country',
'organization_org_city',
'organization_org_country',
'organization_org_state',
'organization_org_state_name',
'organization_dept_type',
'organization_fips_country_code',
'organization_org_duns',
'organization_org_ueis',
'organization_primary_duns',
'organization_primary_uei',
'organization_org_fips',
'organization_org_ipf_code',
'organization_org_zipcode',
'organization_external_org_id',
'award_type',
'activity_code',
'award_amount',
'is_active',
'project_num_split_appl_type_code',
'project_num_split_activity_code',
'project_num_split_ic_code',
'project_num_split_serial_num',
'project_num_split_support_year',
'project_num_split_full_support_year',
'project_num_split_suffix_code',
'program_officers_first_name',
'program_officers_middle_name',
'program_officers_last_name',
'program_officers_full_name',
'agency_ic_admin_code',
'agency_ic_admin_abbreviation',
'agency_ic_admin_name',
'agency_ic_fundings_fy',
'agency_ic_fundings_code',
'agency_ic_fundings_name',
'agency_ic_fundings_abbreviation',
'agency_ic_fundings_total_cost',
'cong_dist',
'project_start_date',
'project_end_date',
'organization_type_name',
'organization_type_code',
'organization_type_is_other',
'full_foa',
'full_study_section_srg_code',
'full_study_section_srg_flex',
'full_study_section_sra_designator_code',
'full_study_section_sra_flex_code',
'full_study_section_group_code',
'full_study_section_name',
'award_notice_date',
'is_new',
'mechanism_code_dc',
'core_project_num',
'terms',
'pref_terms',
'abstract_text',
'project_title',
'phr_text',
'agency_code',
'covid_response',
'arra_funded',
'budget_start',
'budget_end',
'cfda_code',
'funding_mechanism',
'direct_cost_amt',
'indirect_cost_amt',
'project_detail_url',
'date_added'
]

row = []

for i in range (0,len(header)):
    row.append(header[i])

row.append("\n")

writer_mt.writerow(row)
row = []

for i in data["results"]:
    row.append(checkEmptyValue(i["appl_id"]))
    row.append(checkEmptyValue(i["subproject_id"]))
    row.append(checkEmptyValue(i["fiscal_year"]))
    row.append(checkEmptyValue(i["project_num"]))
    row.append(checkEmptyValue(i["project_serial_num"]))

    if i["organization"]:
        row.append(checkEmptyValue(i["organization"]["org_name"]))
        row.append(checkEmptyValue(i["organization"]["city"]))
        row.append(checkEmptyValue(i["organization"]["country"]))
        row.append(checkEmptyValue(i["organization"]["org_city"]))
        row.append(checkEmptyValue(i["organization"]["org_country"]))
        row.append(checkEmptyValue(i["organization"]["org_state"]))
        row.append(checkEmptyValue(i["organization"]["org_state_name"]))
        row.append(checkEmptyValue(i["organization"]["dept_type"]))
        row.append(checkEmptyValue(i["organization"]["fips_country_code"]))

        if i["organization"]["org_duns"]:
            if i["organization"]["org_duns"] is not empty:
                row.append(i["organization"]["org_duns"][0])
            else:
                row.append("")
        else:
            row.append("")

        if i["organization"]["org_ueis"]:
            if i["organization"]["org_ueis"] is not empty:
                row.append(i["organization"]["org_ueis"][0])
            else:
                row.append("")
        else:
            row.append("")

        row.append(checkEmptyValue(i["organization"]["primary_duns"]))
        row.append(checkEmptyValue(i["organization"]["primary_uei"]))
        row.append(checkEmptyValue(i["organization"]["org_fips"]))
        row.append(checkEmptyValue(i["organization"]["org_ipf_code"]))
        row.append(checkEmptyValue(i["organization"]["org_zipcode"]))
        row.append(checkEmptyValue(i["organization"]["external_org_id"]))

    else:
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")

    row.append(checkEmptyValue(i["award_type"]))
    row.append(checkEmptyValue(i["activity_code"]))
    row.append(checkEmptyValue(i["award_amount"]))

    if i["is_active"] is not empty:
        row.append(i["is_active"])
    else:
        row.append("")

    if i["project_num_split"]:
        row.append(checkEmptyValue(i["project_num_split"]["appl_type_code"]))
        row.append(checkEmptyValue(i["project_num_split"]["activity_code"]))
        row.append(checkEmptyValue(i["project_num_split"]["ic_code"]))
        row.append(checkEmptyValue(i["project_num_split"]["serial_num"]))
        row.append(checkEmptyValue(i["project_num_split"]["support_year"]))
        row.append(checkEmptyValue(i["project_num_split"]["full_support_year"]))
        row.append(checkEmptyValue(i["project_num_split"]["suffix_code"]))
    else:
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")

    if i["program_officers"]:
        if i["program_officers"] is not empty:
            row.append(i["program_officers"][0]["first_name"])
            row.append(i["program_officers"][0]["middle_name"])
            row.append(i["program_officers"][0]["last_name"])
            row.append(i["program_officers"][0]["full_name"])
        else:
            row.append("")
            row.append("")
            row.append("")
            row.append("")
    else:
        row.append("")
        row.append("")
        row.append("")
        row.append("")

    if i["agency_ic_admin"]:
        row.append(checkEmptyValue(i["agency_ic_admin"]["code"]))
        row.append(checkEmptyValue(i["agency_ic_admin"]["abbreviation"]))
        row.append(checkEmptyValue(i["agency_ic_admin"]["name"]))
    else:
        row.append("")
        row.append("")
        row.append("")

    if i["agency_ic_fundings"]:
        if i["agency_ic_fundings"] is not empty:
            row.append(i["agency_ic_fundings"][0]["fy"])
            row.append(i["agency_ic_fundings"][0]["code"])
            row.append(i["agency_ic_fundings"][0]["name"])
            row.append(i["agency_ic_fundings"][0]["abbreviation"])
            row.append(i["agency_ic_fundings"][0]["total_cost"])
        else:
            row.append("")
            row.append("")
            row.append("")
            row.append("")
            row.append("")
    else:
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")

    row.append(checkEmptyValue(i["cong_dist"]))
    row.append(checkEmptyValue(i["project_start_date"]))
    row.append(checkEmptyValue(i["project_end_date"]))

    if i["organization_type"]:
        row.append(checkEmptyValue(i["organization_type"]["name"]))
        row.append(checkEmptyValue(i["organization_type"]["code"]))

        if i["organization_type"]["is_other"] is not empty:
            row.append(i["organization_type"]["is_other"])
        else:
            row.append("")
    else:
        row.append("")
        row.append("")
        row.append("")

    row.append(checkEmptyValue(i["full_foa"]))
    
    if i["full_study_section"]:
        row.append(checkEmptyValue(i["full_study_section"]["srg_code"]))
        row.append(checkEmptyValue(i["full_study_section"]["srg_flex"]))
        row.append(checkEmptyValue(i["full_study_section"]["sra_designator_code"]))
        row.append(checkEmptyValue(i["full_study_section"]["sra_flex_code"]))
        row.append(checkEmptyValue(i["full_study_section"]["group_code"]))
        row.append(checkEmptyValue(i["full_study_section"]["name"]))
    else:
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")

    row.append(checkEmptyValue(i["award_notice_date"]))

    if i["is_new"] is not empty:
        row.append(i["is_new"])
    else:
        row.append("")
    
    row.append(checkEmptyValue(i["mechanism_code_dc"]))
    row.append(checkEmptyValue(i["core_project_num"]))
    row.append(checkEmptyValue(i["terms"]))
    row.append(checkEmptyValue(i["pref_terms"]))
    row.append(checkEmptyValue(i["abstract_text"]))
    row.append(checkEmptyValue(i["project_title"]))
    row.append(checkEmptyValue(i["phr_text"]))
    row.append(checkEmptyValue(i["agency_code"]))
    row.append(checkEmptyValue(i["covid_response"]))
    row.append(checkEmptyValue(i["arra_funded"]))
    row.append(checkEmptyValue(i["budget_start"]))
    row.append(checkEmptyValue(i["budget_end"]))
    row.append(checkEmptyValue(i["cfda_code"]))
    row.append(checkEmptyValue(i["funding_mechanism"]))
    row.append(checkEmptyValue(i["direct_cost_amt"]))
    row.append(checkEmptyValue(i["indirect_cost_amt"]))
    row.append(checkEmptyValue(i["project_detail_url"]))
    row.append(checkEmptyValue(i["date_added"]))

    writer_mt.writerow(row)
    row = []

f_mt.close()




#Principal Investigators
header = []
row = []

f_pi = open('nih_reporter_pi_table.csv', 'w', encoding='UTF8', newline='\n')

writer_pi = csv.writer(f_pi)

header = [
'appl_id',
'principal_investigators_profile_id',
'principal_investigators_first_name',
'principal_investigators_middle_name',
'principal_investigators_last_name',
'principal_investigators_is_contact_pi',
'principal_investigators_full_name',
'principal_investigators_title',
'contact_pi_name'
]

row = []

for i in range (0,len(header)):
    row.append(header[i])

writer_pi.writerow(row)
row = []

for i in data["results"]:
    if i["principal_investigators"]:
        if i["principal_investigators"] is not empty:
            for j in range (0,len(i["principal_investigators"])): 
                row.append(i["appl_id"])
                row.append(i["principal_investigators"][j]["profile_id"])
                row.append(i["principal_investigators"][j]["first_name"])
                row.append(i["principal_investigators"][j]["middle_name"])
                row.append(i["principal_investigators"][j]["last_name"])
                row.append(i["principal_investigators"][j]["is_contact_pi"])
                row.append(i["principal_investigators"][j]["full_name"])
                row.append(i["principal_investigators"][j]["title"])
                if i["contact_pi_name"]:
                    row.append(i["contact_pi_name"])
                else:
                    row.append("")
                writer_pi.writerow(row)
                row = []

f_pi.close()

#Spending categories
header = []
row = []

f_sc = open('nih_reporter_spending_table.csv', 'w', encoding='UTF8', newline='\n')

writer_sc = csv.writer(f_sc)

header = [
'appl_id',
'spending_category_id',
'spending_category_name',
]

row = []

for i in range (0,len(header)):
    row.append(header[i])

writer_sc.writerow(row)
row = []

for i in data["results"]:
    if i["spending_categories"]:
        if i["spending_categories"] is not empty:
            for j in range (0,len(i["spending_categories"])): 
                row.append(i["appl_id"])
                row.append(i["spending_categories"][j])
                temp = i["spending_categories_desc"].split(';')
                row.append(temp[j].strip())

                writer_sc.writerow(row)
                row = []

f_sc.close()