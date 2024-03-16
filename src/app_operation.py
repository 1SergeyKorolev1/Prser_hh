def app_operation(sp):
    sp.create_database(sp.name_db)
    employers = sp.api.get_employers_api(sp.link_hh_employers)
    for i in employers:
        print(i)