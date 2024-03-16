def app_operation(sp):
    sp.create_database(sp.name_db)
    sp.create_table(sp.name_db, sp.name_table_employers, sp.command_employers, sp.work_with_db)
    employers_list = sp.api.get_employers_api(sp.link_hh_employers)
    if employers_list != 0:
        sp.write_employers_in_db(employers_list, sp.name_db, sp.work_with_db, sp.name_table_employers,
                                 sp.command_insert_employers)
    else:
        pass
