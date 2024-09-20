from aiogram.utils.keyboard import InlineKeyboardBuilder




# Inline клавіатура для списку фільмів
def build_films_keyboard(films: list):
   builder = InlineKeyboardBuilder()
   for index, film in enumerate(films):
       builder.button(text=film.get("title"), callback_data=f"film_{index}")
   return builder.as_markup()


from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove


from ..data import get_films
from ..keyboards import build_films_keyboard




film_router = Router()




#Обробник для команди /films та повідомлення із текстом films
@film_router.message(Command("films"))
@film_router.message(F.text.casefold() == "films")
async def show_films_command(message: Message, state: FSMContext) -> None:
   films = get_films()
   keyboard = build_films_keyboard(films)
   await message.answer(
       text="Виберіть будь-який фільм",
       reply_markup=keyboard,
   )

@film_router.callback_query(F.data.startswith("film_"))
async def show_film_details(callback: CallbackQuery, state: FSMContext) -> None:
   film_id = int(callback.data.split("_")[-1])
   film = get_film(film_id)
   text = f"Назва:{hbold(film.get('title'))}\nОпис:{hbold(film.get('desc'))}\nРейтинг:{hbold(film.get('rating'))}"
   photo_id = film.get('photo')
   url = film.get('url')
   await callback.message.answer_photo(photo_id)
   await edit_or_answer(callback.message, text, build_film_details_keyboard(url))



   from aiogram.utils.keyboard import InlineKeyboardBuilder




def build_films_keyboard(films: list):
   builder = InlineKeyboardBuilder()
   for index, film in enumerate(films):
       builder.button(text=film.get("title"), callback_data=f"film_{index}")
   return builder.as_markup()


def build_film_details_keyboard(url):
   builder = InlineKeyboardBuilder()
   builder.button(text="Перейти за посиланням", url=url)
   builder.button(text="Go back", callback_data="back")
   return builder.as_markup()
  


def build_menu_keyboard():
   builder = InlineKeyboardBuilder()
   builder.button(text="Go back", callback_data="back")
   return builder.as_markup()
