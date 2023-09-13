import threading

# Crear un semáforo con un número de permisos inicial
semaforo = threading.Semaphore(3)  # Límite de 3 personas en la piscina

def ingresar_piscina(persona):
    print(f'{persona} está esperando para ingresar a la piscina.')
    with semaforo:
        print(f'{persona} ha ingresado a la piscina.')
        # Simulamos tiempo en la piscina
        threading.Event().wait(2)
        print(f'{persona} ha salido de la piscina.')

# Creamos hilos que representan a personas que quieren ingresar a la piscina
persona1 = threading.Thread(target=ingresar_piscina, args=('Persona 1',))
persona2 = threading.Thread(target=ingresar_piscina, args=('Persona 2',))
persona3 = threading.Thread(target=ingresar_piscina, args=('Persona 3',))
persona4 = threading.Thread(target=ingresar_piscina, args=('Persona 4',))

# Iniciamos los hilos
persona1.start()
persona2.start()
persona3.start()
persona4.start()

# Esperamos a que todos los hilos terminen
persona1.join()
persona2.join()
persona3.join()
persona4.join()


