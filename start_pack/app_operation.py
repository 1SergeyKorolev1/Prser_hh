def app_operation(sp):
    employers = sp.api.get_employers_api(sp.link_hh_employers)
    for i in employers:
        print(i)