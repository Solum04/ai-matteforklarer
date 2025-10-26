from ai_matte import MathTutor

def main():
    tutor = MathTutor()
    for p in ["3x + 5 = 11", "10x-20=0", "x^2+1=0"]:
        print("==>", p)
        print(tutor.explain(p))
        print()

if __name__ =='__main__':
    main()
