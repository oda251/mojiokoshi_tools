import flet as ft


def list_to_str(lst):
    return ", ".join(map(lambda f: f.name, lst))


def main(page: ft.Page):
    # Page Configuration
    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[ft.Locale("ja", "JP"), ft.Locale("en", "US")],
        current_locale=ft.Locale("ja", "JP"),
    )

    page.fonts = {
        "Noto Sans JP": "https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100..900&display=swap"
    }
    page.theme = ft.Theme(
        font_family="Noto Sans JP",
    )

    # Attributes
    selected_files = []

    # File Picker logic
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files = e.files
        SelectedFiles.value = list_to_str(selected_files)
        SelectedFiles.update()

    # Components
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    SelectedFiles = ft.Text(value=list_to_str(selected_files))
    FilePicker = ft.Row(
        [
            ft.ElevatedButton(
                "Pick files",
                icon=ft.Icons.UPLOAD_FILE,
                on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
            ),
            SelectedFiles,
        ]
    )

    page.overlay.append(pick_files_dialog)  # Move this line before adding the container

    container = ft.Column()
    container.controls.append(FilePicker)

    page.add(container)


ft.app(target=main)
