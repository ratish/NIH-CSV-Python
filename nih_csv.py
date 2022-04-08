from numpy import empty
import requests
import json
import csv

headers = {
    'accept': 'application/json',
}

json_data = {
    "criteria": {
        "org_names": ["UNIVERSITY OF ARIZONA"]
    },
    "limit": 500
}

response = requests.post('https://api.reporter.nih.gov/v2/projects/search', headers=headers, json=json_data)

data = json.loads(response.content)

f = open("nih_csv_test.json", "w")
f.write(json.dumps(data, indent=2))
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
    if i["appl_id"]:
        row.append(i["appl_id"])
    else:
        row.append("")

    if i["subproject_id"]:
        row.append(i["subproject_id"])
    else:
        row.append("")

    if i["fiscal_year"]:
        row.append(i["fiscal_year"])
    else:
        row.append("")

    if i["project_num"]:
        row.append(i["project_num"])
    else:
        row.append("")

    if i["project_serial_num"]:
        row.append(i["project_serial_num"])
    else:
        row.append("")

    if i["organization"]:
        if i["organization"]["org_name"]:
            row.append(i["organization"]["org_name"])
        else:
            row.append("")

        if i["organization"]["city"]:
            row.append(i["organization"]["city"])
        else:
            row.append("")

        if i["organization"]["country"]:
            row.append(i["organization"]["country"])
        else:
            row.append("")

        if i["organization"]["org_city"]:
            row.append(i["organization"]["org_city"])
        else:
            row.append("")

        if i["organization"]["org_country"]:
            row.append(i["organization"]["org_country"])
        else:
            row.append("")

        if i["organization"]["org_state"]:
            row.append(i["organization"]["org_state"])
        else:
            row.append("")

        if i["organization"]["org_state_name"]:
            row.append(i["organization"]["org_state_name"])
        else:
            row.append("")

        if i["organization"]["dept_type"]:
            row.append(i["organization"]["dept_type"])
        else:
            row.append("")

        if i["organization"]["fips_country_code"]:
            row.append(i["organization"]["fips_country_code"])
        else:
            row.append("")

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

        if i["organization"]["primary_duns"]:
            row.append(i["organization"]["primary_duns"])
        else:
            row.append("")

        if i["organization"]["primary_uei"]:
            row.append(i["organization"]["primary_uei"])
        else:
            row.append("")

        if i["organization"]["org_fips"]:
            row.append(i["organization"]["org_fips"])
        else:
            row.append("")

        if i["organization"]["org_ipf_code"]:
            row.append(i["organization"]["org_ipf_code"])
        else:
            row.append("")

        if i["organization"]["org_zipcode"]:
            row.append(i["organization"]["org_zipcode"])
        else:
            row.append("")

        if i["organization"]["external_org_id"]:
            row.append(i["organization"]["external_org_id"])
        else:
            row.append("")
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

    if i["award_type"]:
        row.append(i["award_type"])
    else:
        row.append("")

    if i["activity_code"]:
        row.append(i["activity_code"])
    else:
        row.append("")

    if i["award_amount"]:
        row.append(i["award_amount"])
    else:
        row.append("")

    if i["is_active"] is not empty:
        row.append(i["is_active"])
    else:
        row.append("")

    if i["project_num_split"]:
        if i["project_num_split"]["appl_type_code"]:
            row.append(i["project_num_split"]["appl_type_code"])
        else:
            row.append("")

        if i["project_num_split"]["activity_code"]:
            row.append(i["project_num_split"]["activity_code"])
        else:
            row.append("")

        if i["project_num_split"]["ic_code"]:
            row.append(i["project_num_split"]["ic_code"])
        else:
            row.append("")

        if i["project_num_split"]["serial_num"]:
            row.append(i["project_num_split"]["serial_num"])
        else:
            row.append("")

        if i["project_num_split"]["support_year"]:
            row.append(i["project_num_split"]["support_year"])
        else:
            row.append("")

        if i["project_num_split"]["full_support_year"]:
            row.append(i["project_num_split"]["full_support_year"])
        else:
            row.append("")

        if i["project_num_split"]["suffix_code"]:
            row.append(i["project_num_split"]["suffix_code"])
        else:
            row.append("")
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
        if i["agency_ic_admin"]["code"]:
            row.append(i["agency_ic_admin"]["code"])
        else:
            row.append("")

        if i["agency_ic_admin"]["abbreviation"]:
            row.append(i["agency_ic_admin"]["abbreviation"])
        else:
            row.append("")

        if i["agency_ic_admin"]["name"]:
            row.append(i["agency_ic_admin"]["name"])
        else:
            row.append("")
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

    if i["cong_dist"]:
        row.append(i["cong_dist"])
    else:
        row.append("")

    if i["project_start_date"]:
        row.append(i["project_start_date"])
    else:
        row.append("")

    if i["project_end_date"]:
        row.append(i["project_end_date"])
    else:
        row.append("")

    if i["organization_type"]:
        if i["organization_type"]["name"]:
            row.append(i["organization_type"]["name"])
        else:
            row.append("")

        if i["organization_type"]["code"]:
            row.append(i["organization_type"]["code"])
        else:
            row.append("")

        if i["organization_type"]["is_other"] is not empty:
            row.append(i["organization_type"]["is_other"])
        else:
            row.append("")
    else:
        row.append("")
        row.append("")
        row.append("")


    if i["full_foa"]:
        row.append(i["full_foa"])
    else:
        row.append("")

    if i["full_study_section"]:
        if i["full_study_section"]["srg_code"]:
            row.append(i["full_study_section"]["srg_code"])
        else:
            row.append("")

        if i["full_study_section"]["srg_flex"]:
            row.append(i["full_study_section"]["srg_flex"])
        else:
            row.append("")

        if i["full_study_section"]["sra_designator_code"]:
            row.append(i["full_study_section"]["sra_designator_code"])
        else:
            row.append("")

        if i["full_study_section"]["sra_flex_code"]:
            row.append(i["full_study_section"]["sra_flex_code"])
        else:
            row.append("")

        if i["full_study_section"]["group_code"]:
            row.append(i["full_study_section"]["group_code"])
        else:
            row.append("")

        if i["full_study_section"]["name"]:
            row.append(i["full_study_section"]["name"])
        else:
            row.append("")
    else:
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")

    if i["award_notice_date"]:
        row.append(i["award_notice_date"])
    else:
        row.append("")

    if i["is_new"] is not empty:
        row.append(i["is_new"])
    else:
        row.append("")

    if i["mechanism_code_dc"]:
        row.append(i["mechanism_code_dc"])
    else:
        row.append("")

    if i["core_project_num"]:
        row.append(i["core_project_num"])
    else:
        row.append("")

    if i["terms"]:
        row.append(i["terms"])
    else:
        row.append("")

    if i["pref_terms"]:
        row.append(i["pref_terms"])
    else:
        row.append("")

    if i["abstract_text"]:
        row.append(i["abstract_text"])
    else:
        row.append("")

    if i["project_title"]:
        row.append(i["project_title"])
    else:
        row.append("")

    if i["phr_text"]:
        row.append(i["phr_text"])
    else:
        row.append("")

    if i["agency_code"]:
        row.append(i["agency_code"])
    else:
        row.append("")

    if i["covid_response"]:
        row.append(i["covid_response"])
    else:
        row.append("")

    if i["arra_funded"]:
        row.append(i["arra_funded"])
    else:
        row.append("")

    if i["budget_start"]:
        row.append(i["budget_start"])
    else:
        row.append("")

    if i["budget_end"]:
        row.append(i["budget_end"])
    else:
        row.append("")

    if i["cfda_code"]:
        row.append(i["cfda_code"])
    else:
        row.append("")

    if i["funding_mechanism"]:
        row.append(i["funding_mechanism"])
    else:
        row.append("")

    if i["direct_cost_amt"]:
        row.append(i["direct_cost_amt"])
    else:
        row.append("")

    if i["indirect_cost_amt"]:
        row.append(i["indirect_cost_amt"])
    else:
        row.append("")

    if i["project_detail_url"]:
        row.append(i["project_detail_url"])
    else:
        row.append("")

    if i["date_added"]:
        row.append(i["date_added"])
    else:
        row.append("")
    
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



