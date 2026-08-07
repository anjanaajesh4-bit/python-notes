age=20
has_id=True
is_banned=False
if age>=18 and has_id:
    print("age and id satisfied")

if age<18 and not has_id:
      print("age and id not satisfied")

if not is_banned:
    print("you are not allowed to enter")