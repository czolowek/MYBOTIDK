from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.client.default import DefaultBotProperties
from keyboards import  build_films_keyboard
from .routers import film_router #Імпорт роутера логіки з фільмами
from .handler import get_films
from .film import film_router






# Завантажимо дані середовища з файлу .env(За замовчуванням)
load_dotenv()


# Усі обробники варто закріплювати за Router або Dispatcher
root_router = Router()


# Обробник для команди /start
@root_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
   await message.answer(f"дарова, {hbold(message.from_user.full_name)}!")




# Головна функція пакету
async def main() -> None:
   # Дістанемо токен бота з середовища
   TOKEN = getenv("BOT_TOKEN")
   # Створимо об'єкт Bot
   bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


   dp = Dispatcher()
   dp.include_router(root_router)
   # Почнемо обробляти події для бота
   await dp.start_polling(bot)




from .routers import film_router #Імпорт роутера логіки з фільмами


# Завантажимо дані середовища з файлу .env(За замовчуванням)

load_dotenv()




# Усі обробники варто закріплювати за Router або Dispatcher
root_router = Router()
root_router.include_routers(film_router,) #Включення роутера в головний


# Обробник для команди /start
@root_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
   await message.answer(f"Вітаю, {hbold(message.from_user.full_name)}!")






async def main() -> None:
   # Дістанемо токен бота з середовища
   TOKEN = getenv("BOT_TOKEN")
   # Створимо об'єкт Bot
   bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
  
   dp = Dispatcher()
   dp.include_router(root_router)
   # Почнемо обробляти події для бота
   await dp.start_polling(bot)

async def edit_or_answer(message: Message, text: str, keyboard, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)

def get_film(id:int=0, f_path:str = "app/data/films.json")->dict:
   return get_films(f_path)[id]

