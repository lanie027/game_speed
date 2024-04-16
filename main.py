base_attack_speed = input("Enter the Base Attack Speed:");
base_attack_speed = float(base_attack_speed)
bonus_attack_speed = input ("Enter the bonus attack speed %: ")
bonus_attack_speed = float(bonus_attack_speed)
divide = bonus_attack_speed / 100
level = input("Enter the level: ")
level = float(level)
sub = level - 1
Current_Attack_Speed = base_attack_speed * (1 + (divide * (sub)))
final_CAP = round(Current_Attack_Speed * 1000) / 1000.0
print("The character current attack speed is", final_CAP)