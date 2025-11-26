import MariageStable
import preferences_generator
import SatisfactionCalculator
import argparse
from flaskr.wepApp import WebApp

def cli_launch(verbose : bool, number : int) -> None:
    students, schools = preferences_generator.gen_pref(number)
    preferences_generator.print_pref(students, schools)
    m = MariageStable.MariageStable(students,schools)
    matches = m.solve(verbose)
    print("Matches :", matches)

    if not verbose:
        return
    
    s = SatisfactionCalculator.SatisfactionCalculator(students,schools,matches)

    print("Students satisfaction :", s.getStudentsSatisfaction())
    print("Schools satisfaction :", s.getSchoolsSatisfaction())
    print("Average student satisfaction :", s.getAverageStudentSatisfaction())
    print("Average school satisfaction :", s.getAverageSchoolSatisfaction())
    print("Average global satisfaction :", s.getGlobalSatisfaction())

def web_launch():
    app = WebApp()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='Démo Mariage stable',
                        description='Génère des préférence et lance le Mariage Stable',
                        epilog='Use -W or --web to launch this in web')
    parser.print_help()
    
    parser.add_argument('-n', '--number', default=5, type=int)
    parser.add_argument('-w', '--web', action='store_true', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    args = parser.parse_args()

    if args.web:
        web_launch()
    else:  
        cli_launch(args.verbose, args.number)