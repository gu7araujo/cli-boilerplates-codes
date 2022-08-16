class Repo(object):
    id = 1
    name = ""
    link = ""
    readme = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, id, name, link, readme):
        self.id = id
        self.name = name
        self.link = link
        self.readme = readme


#Swift repos
readme_swift_1 = """
- Swift 5 + Clean Architecture + MVVM

Description:
iOS Project implemented with Clean Layered Architecture and MVVM. (Can be used as Template project by replacing item name “Movie”). More information in medium post.

@Author: kudoleh Oleh
"""

readme_swift_2 = """
— Combine + UIKit + MVVM

Description:
This simple app consists of two screens and includes basic concepts that are common usecases for using reactive programming.
First screen showcases offline validation of text fields (login screen as an example).
Second screen presents fetching data from public and free API.

@Author: Michał Cichecki
"""

readme_swift_3 = """
— SwiftVIPER

Description:
SwiftyVIPER allows easy use of VIPER architecture throughout your iOS application.

@Author: Cody Winton
"""

readme_swift_4 = """
- Swift 4 and Using MVVM architecture(Rxswfit + Moya) to implement Github client demo.

Features:
Swift 4
RxSwift
Moya (networking layer)
MVVM architecture implement
TableView Pagination
RxDataSources
Codable (Object mapping)
Coordinator

@Author: Leo Liu
"""

swift_1 = Repo(1, "iOS-Clean-Architecture-MVVM", "https://github.com/kudoleh/iOS-Clean-Architecture-MVVM.git", readme=readme_swift_1)
swift_2 = Repo(2, "Combine-MVVM", "https://github.com/mcichecki/combine-mvvm.git", readme=readme_swift_2)
swift_3 = Repo(3, "Swift-Viper-Arch", "https://github.com/pablobarcos/SwiftViperArch.git", readme=readme_swift_3)
swift_4 = Repo(4, "Swift-Rxswift-Moya", "https://github.com/liuznsn/boilerplate", readme=readme_swift_4)

#C# repos
readme_CSharp_1 = """
— Sample .NET Core REST API CQRS implementation with raw SQL and DDD using Clean Architecture.

Description:
Sample .NET Core REST API application implemented with basic CQRS approach and Domain Driven Design  (DDD).

@Author: Kamil Grzybek


— Template iOS App using Clean Architecture and MVVM

Description:
iOS Project implemented with Clean Layered Architecture and MVVM. (Can be used as Template project by replacing item name “Movie”). More information in medium post: Medium Post about Clean Architecture + MVVM

@Author: Kudoleh Oleh
"""

CSharp_1 = Repo(5, "Sample-Dotnet-Core-Cqrs-Api", "https://github.com/kgrzybek/sample-dotnet-core-cqrs-api", readme=readme_CSharp_1)

#TS repos
readme_ts_1 = """
— A Node.js CQRS/ES Swagger API Microservice Boilerplate

Description: 
This is an application boilerplate that demonstrates how to use Nest.js and Event Store to create a RESTful Users API microservice.
Please note that commands have been implemented and they do write into the Event Store, however, queries for denormalized views have some boilerplate but it is up to you to implement them using your favorite database technology of choice.
In case you don't feel like downloading dependencies locally, I've added support for Docker so follow those instructions in "Running the app" and you'll have everything up and running in less than 2 minutes.

@Author: Qasim Soomro
"""

ts_1 = Repo(6, "Examples-Nodejs-Cqrs-Es-Swagger", "https://github.com/qas/examples-nodejs-cqrs-es-swagger", readme=readme_ts_1)


from loader import Loader
from simple_term_menu import TerminalMenu
import subprocess
import os

def download_repo(repo: Repo):
    loader = Loader(f"Cloning into '{repo.name}'...", "done", 0.5).start()
    if os.path.isdir('./clones') == False:
        os.mkdir("clones")

    result = subprocess.run(['git', '-C', 'clones', 'clone', repo.link], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
    loader.stop()

def list_stacks():
    stacks = ["SWIFT", "C#", "TYPESCRIPT"]
    terminal_menu = TerminalMenu(stacks, title="Escolha a stack que deseja listar os modelos")
    choice_stack = terminal_menu.show()
    
    if stacks[choice_stack] == "SWIFT":
        list_repos_by_stack_swift()
    elif stacks[choice_stack] == "C#":
        list_repos_by_stack_csahrp()
    else:
        list_repos_by_stack_typescript()


def list_repos_by_stack_typescript():
    typescript_repos = [ts_1]
    typescript_repos_names = [ts_1.name, "Voltar"]
    terminal_menu = TerminalMenu(typescript_repos_names, title="Escolha o boilerplate de TS que deseja ver mais")
    choice_typescript_boilerplate = terminal_menu.show()
    if typescript_repos_names[choice_typescript_boilerplate] == "Voltar":
        list_stacks()
    else:
        show_readme_and_download(typescript_repos[choice_typescript_boilerplate], list_repos_by_stack_typescript)

def list_repos_by_stack_csahrp():
    csharp_repos = [CSharp_1]
    csharp_repos_names = [CSharp_1.name, "Voltar"]
    terminal_menu = TerminalMenu(csharp_repos_names, title="Escolha o boilerplate de C# que deseja ver mais")
    choice_csharp_boilerplate = terminal_menu.show()
    if csharp_repos_names[choice_csharp_boilerplate] == "Voltar":
        list_stacks()
    else:
        show_readme_and_download(csharp_repos[choice_csharp_boilerplate], list_repos_by_stack_csahrp)

def list_repos_by_stack_swift():
    swift_repos = [swift_1, swift_2, swift_3, swift_4]
    swift_repos_names = [swift_1.name, swift_2.name, swift_3.name, swift_4.name, "Voltar"]
    terminal_menu = TerminalMenu(swift_repos_names, title="Escolha o boilerplate de SWIFT que deseja ver mais")
    choice_repo_swift = terminal_menu.show()
    if swift_repos_names[choice_repo_swift] == "Voltar":
        list_stacks()
    else:
        show_readme_and_download(swift_repos[choice_repo_swift], list_repos_by_stack_swift)

def show_readme_and_download(repo: Repo, again):
    terminal_menu = TerminalMenu(["Baixar", "Voltar"], title="LEIA O README DO BOILERPLATE E CONFIRME SE DESEJA BAIXAR O REPOSITÓRIO OU VOLTAR\n" + repo.readme)
    choice_option = terminal_menu.show()
    if choice_option == 1:
        again()
    else:
        download_repo(repo)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    list_stacks()


if __name__ == '__main__':
    main()