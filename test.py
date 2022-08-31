
def handle_titles(title: str, names: Dict[int, str]) -> List[str]:
    """Determines data to be changed."""

    pattern_handle = {
        'Фамилия': re.compile(r'(?<=\w).+(?=\w)'),
        'Имя': re.compile(r'^$'),
        'Отчество': re.compile(r'^$'),
        'email': re.compile(r'(?<=\w).+(?=\w)'),
        'Телефон': re.compile(r'(?<=\w).+(?=\w)'), 
    }

    return [change_chars(text, pattern_handle[title]) for text in names.values()]


def main() -> None:
    try:
        data = pd.read_excel('data.xlsx').to_dict()
        for title, name in data.items():
            i = 0
            for i in name:
                try:
                    name[i] = int(name[i])
                    if type(name[i]) is int:
                        name[i] = str(name[i])
                except:
                    pass

                if type(name[i]) is float:
                    name[i] = '*****'
                i += 1
        print(data)
        data_edited = {
            title: handle_titles(title, names) for title, names in data.items()
        }
        print(data_edited) 

        result = pd.DataFrame.from_dict(data_edited)
        result.to_excel('data_edited.xlsx')
        
    except Exception as e:
        print(f"Что-то пошло не так: {e}")


if __name__ == "__main__":
    main()
