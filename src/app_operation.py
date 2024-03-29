def app_operation(sp):
    sp.work_with_db.create_database(sp.name_db, sp.password_db)
    sp.create_table(sp.name_db, sp.name_table_employers, sp.command_employers, sp.work_with_db, sp.password_db)
    sp.create_table(sp.name_db, sp.name_table_vacancies, sp.command_vacancies, sp.work_with_db, sp.password_db)
    employers_list = sp.api.get_employers_api(sp.link_hh_employers)
    if employers_list != 0:
        sp.write_data_in_db(employers_list, sp.name_db, sp.work_with_db, sp.name_table_employers,
                            sp.command_insert_employers, sp.name_for_print_employers, sp.password_db)
        for i in employers_list:
            vacancies_list = sp.api.get_vacancies_from_company_api(i[0], sp.link_hh_vacancies, sp.count_vacancies)
            if vacancies_list != 0:
                sp.write_data_in_db(vacancies_list, sp.name_db, sp.work_with_db, sp.name_table_vacancies,
                                    sp.command_insert_vacancies, sp.name_for_print_vacancies, sp.password_db)
        sp.work_with_db.get_companies_and_vacancies_count(sp.work_with_db, sp.name_db, sp.password_db)
        sp.work_with_db.get_all_vacancies(sp.work_with_db, sp.name_db, sp.password_db)
        sp.work_with_db.get_avg_salary(sp.work_with_db, sp.name_db, sp.password_db)
        sp.work_with_db.get_vacancies_with_higher_salary(sp.work_with_db, sp.name_db, sp.password_db)
        keyword = input('Введите ключевое слово для поиска по названию вакансий:')
        sp.work_with_db.get_vacancies_with_keyword(sp.work_with_db, sp.name_db, sp.password_db, keyword)
        keyword = input('Введите ключевое слово для поиска по описанию вакансий:')
        sp.work_with_db.get_vacancies_with_keyword_in_description(sp.work_with_db, sp.name_db, sp.password_db, keyword)
