import argparse
from ai_matte import MathTutor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=["local", "ai"], default="local",
                        help="Velg løser: 'local' (regelbasert) eller 'ai' (LLM)")
    parser.add_argument("problem", nargs="?", default="3x + 5 = 11")
    args = parser.parse_args()


    tutor = MathTutor(engine=args.engine)
    print(tutor.explain(args.problem))


if __name__ =='__main__':
    main()
