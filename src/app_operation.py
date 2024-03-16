def app_operation(sp):
    sp.create_database(sp.name_db)
    sp.create_table(sp.name_db, sp.name_table_employers, sp.command_employers)
    sp.write_employers_in_db(sp.api.get_employers_api(sp.link_hh_employers), sp.name_db)
