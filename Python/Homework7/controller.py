import model
import view


def start():
    choice = ''
    while choice != 8:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
            case 5:
                trash = view.trash_contact()
                model.delete_contact(trash)
            case 6:
                check = view.change_contact()
                change = view.change_contact()
                model.correct_contact(check)
                model.correct_contact(change)
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case _:
                view.input_error() 