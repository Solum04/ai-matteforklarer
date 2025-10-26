from ai_matte.tutor import MathTutor

def main():
    tutor = MathTutor()
    problem = "3x + 5 = 11"
    print(tutor.explain(problem))

if __name__ =='__main__':
    main()
