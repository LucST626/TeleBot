# Importa las clases necesarias para interactuar con la API de Telegram y manejar actualizaciones.
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random  # Importa la librería random para generar números aleatorios.

# Define el comando /start.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Responde al usuario con un mensaje de bienvenida cuando usa el comando /start.
    await update.message.reply_text("¡Hola! Soy tu bot. Usa /hola para saludarme o /aleatorio para un número aleatorio.")

# Define el comando /hola.
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Responde con un mensaje divertido al usar el comando /hola.
    await update.message.reply_text("Bomboclat!!")

# Define el comando /aleatorio.
async def aleatorio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Genera un número aleatorio entre 1 y 100.
    numero = random.randint(1, 100)
    # Responde al usuario con el número aleatorio generado.
    await update.message.reply_text(f"Numeroclat bombo es: {numero}")

# Función principal donde se configura el bot.
def main():
    # Reemplaza 'yourapi' con tu API Key de Telegram para autenticar el bot.
    api_key = "yourapi"
    # Crea una aplicación del bot con la API Key.
    app = ApplicationBuilder().token(api_key).build()

    # Agrega manejadores para los comandos. Cada comando llama a una función específica.
    app.add_handler(CommandHandler("start", start))  # Maneja el comando /start.
    app.add_handler(CommandHandler("hola", hola))  # Maneja el comando /hola.
    app.add_handler(CommandHandler("aleatorio", aleatorio))  # Maneja el comando /aleatorio.

    # Inicia el bot en modo de polling (consulta constante de actualizaciones a Telegram).
    print("El bot está corriendo...")
    app.run_polling()

# Punto de entrada del script. Solo se ejecuta si este archivo es el principal.
if __name__ == "__main__":
    main()
