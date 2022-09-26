import asyncio
import logging

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.exceptions import Throttled
from aiogram.utils.executor import start_polling

from parse import active, genecov, recovered, new, deaths, tests

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    markup2 = InlineKeyboardMarkup(row_width=3)
    item1 = InlineKeyboardButton('Cases', callback_data='cases')
    item2 = InlineKeyboardButton('Recovered', callback_data='recovered')
    item3 = InlineKeyboardButton('New Cases', callback_data='new')
    item4 = InlineKeyboardButton('Active Cases', callback_data='active')
    item5 = InlineKeyboardButton('Deaths', callback_data='deaths')
    item6 = InlineKeyboardButton('Tests', callback_data='tests')
    markup2.add(item1, item2, item3, item4, item5, item6)
    try:
        await dp.throttle('start', rate=5)
        await bot.send_message(message.chat.id, "This bot gives you statistics of Covid-19 in Azerbaijan",
                               reply_markup=markup2)
    except Throttled:
        await message.reply('_Too many requests!_', parse_mode='Markdown')


@dp.message_handler(commands=['help'])
async def helpcom(message: types.Message):
    try:
        await dp.throttle('help', rate=5)
        await bot.send_message(message.chat.id,
                               "This bot takes data from Tebib website and gives them to you."
                               "\n"
                               "\n"
                               "\n/cases - total cases."
                               "\n/recovered - total recovered."
                               "\n/new - new cases."
                               "\n/active - active cases."
                               "\n/deaths - total deaths."
                               "\n/tests - total tests.")
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')
        

@dp.callback_query_handler(text="cases")
async def sdcases(call: types.CallbackQuery):
    try:
        await dp.throttle('cases', rate=5)
        await call.message.answer(f'{genecov()} - Total cases')
        await call.answer()
    except Throttled:
        await call.message.answer("_Too many requests! Try after 5 seconds._", parse_mode='Markdown')


@dp.message_handler(commands=['cases'])
async def sscases(message):
    try:
        await dp.throttle('cases', rate=5)
        await bot.send_message(message.chat.id, f'{genecov()} - Total cases')
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')


@dp.callback_query_handler(text='recovered')
async def sdrecovered(call: types.CallbackQuery):
    try:
        await dp.throttle('recovered', rate=5)
        await call.message.answer(f'{recovered()} - Total recovered')
        await call.answer()
    except Throttled:
        await call.message.answer("_Too many requests! Try after 5 seconds._", parse_mode='Markdown')


@dp.message_handler(commands=['recovered'])
async def ssrecovered(message: types.Message):
    try:
        await dp.throttle('recovered', rate=5)
        await bot.send_message(message.chat.id, f'{recovered()} - Total recovered')
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode="Markdown")


@dp.callback_query_handler(text='new')
async def sdnew(call: types.CallbackQuery):
    try:
        await dp.throttle('new', rate=5)
        await call.message.answer(f'{new()} - New infected')
        await call.answer()
    except Throttled:
        await call.message.answer("_Too many requests! Try after 5 seconds._", parse_mode='Markdown')


@dp.message_handler(commands=['new'])
async def ssnew(message: types.Message):
    try:
        await dp.throttle('new', rate=5)
        await bot.send_message(message.chat.id, f'{new()} - New infected')
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')


@dp.callback_query_handler(text='active')
async def sdactive(call: types.CallbackQuery):
    try:
        await dp.throttle('active', rate=5)
        await call.message.answer(f'{active()} - Active cases')
        await call.answer()
    except Throttled:
        await call.message.answer("_Too many requests! Try after 5 seconds._", parse_mode='Markdown')


@dp.message_handler(commands=['active'])
async def ssactive(message: types.Message):
    try:
        await dp.throttle('active', rate=5)
        await bot.send_message(message.chat.id, f'{active()} - Active cases')
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')


@dp.callback_query_handler(text='deaths')
async def sddeaths(call: types.CallbackQuery):
    try:
        await dp.throttle('deaths', rate=5)
        await call.message.answer(f'{deaths()} - Total deaths')
        await call.answer()
    except Throttled:
        await call.message.answer("_Too many requests! Try after 5 seconds._", parse_mode='Markdown')


@dp.message_handler(commands=['deaths'])
async def ssdeaths(message: types.Message):
    try:
        await dp.throttle('deaths', rate=5)
        await bot.send_message(message.chat.id, f'{deaths()} - Total deaths')
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')


@dp.callback_query_handler(text='tests')
async def sdtests(call: types.CallbackQuery):
    try:
        await dp.throttle('tests', rate=5)
        await call.message.answer(f'{tests()} - Total tests')
        await call.answer()
    except Throttled:
        await call.message.answer('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')


@dp.message_handler(commands=['tests'])
async def sstests(message: types.Message):
    try:
        await dp.throttle('tests', rate=5)
        await bot.send_message(message.chat.id, f'{tests()} - Total tests')
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')


@dp.message_handler()
async def any(message: Message):
    try:
        await dp.throttle('help', rate=5)
        await bot.send_message(message.chat.id,
                               "This bot takes data from Tebib website and gives them to you."
                               "\n"
                               "\n"
                               "\n/cases - total cases."
                               "\n/recovered - total recovered."
                               "\n/new - new cases."
                               "\n/active - active cases."
                               "\n/deaths - total deaths."
                               "\n/tests - total tests.")
    except Throttled:
        await message.reply('_Too many requests! Try after 5 seconds._', parse_mode='Markdown')


if __name__ == '__main__':
    start_polling(dp, skip_updates=True)
