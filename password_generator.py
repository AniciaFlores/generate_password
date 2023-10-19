import random
import string

def generate_password(length, use_digits=True, use_uppercase=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_special_chars:
        characters += string.punctuation
        
    if not characters:
        print("Lo siento, no se puede generar contraseñas sin caracteres.")
        return 
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("¡Bienvenido al Generador de Contraseñas!")
    
    counter = 1
    
    while True:
        counter += 1
        
        min_length = 8
        max_length = 50        
        length = int(input(f"Dime el número de caracteres que debe tener tu contraseña (entre {min_length} y {max_length}): "))
        
        if length < min_length:
            print(f"La longitud mínima de la contraseña es de {min_length} caracteres. Por favor, elige una longitud válida.")
            continue
        
        if length > max_length:
            print(f"La longitud máxima permitida es de {max_length} caracteres. Por favor, elige una longitud válida.")
            continue
        
        if length < min_length or length > max_length:
            print(f"La longitud de la contraseña debe estar entre {min_length} y {max_length}.")
            continue
        
        use_digits = input("¿Incluyo números? (S/N): ").strip().lower() == 's'
        use_upercase = input("¿Incluyo letras mayúsculas? (S/N): ").strip().lower() == 's'
        use_special_chars = input("¿Incluyo caracteres especiales? (S/N): ").strip().lower() == 's'
        
        extra_data = input("Si deseas inluir palabras o datos numéricos adicionales, ingrésalos aquí (o presiona Enter para omitir): ")
    
        password = generate_password(length, use_digits, use_upercase, use_special_chars)
        
        if extra_data:
            password += extra_data
        
        if password:
            print(f"Listo, aquí está tu Contraseña # {counter}:", password)
        else: 
            print("¡Lo siento, no se pudo generar la contraseña! Realiza otro intento")
            
        another_attempt = input("¿Deseas generar otra contraseña? (S/N): ").strip().lower()
        if another_attempt != 's':
            print("¡Gracias por usar el Generador de Contraseñas! ¡Hasta luego!")
            break