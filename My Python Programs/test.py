def setscore(score):
          _score = score
          if _score <= 39 :
               grade = 'F'
          elif _score<= 45 and _score >= 40:
               grade = 'E'
          elif _score <= 49 and _score >=46:
               grade = 'D'
          elif _score <=59 and _score >=50:
               grade = 'C'
          elif _score <=69 and _score >=60:
               grade = 'B'
          elif self._score >= 70:
               grade = 'A'
          else:
               grade = False

          print(grade)
         # self._grade = grade

setscore(23)
