import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from database import TaskDatabase
from PIL import Image, ImageDraw, ImageFont
import textwrap

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
DB_PATH = os.getenv('DATABASE_PATH', 'tasks.db')

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)
db = TaskDatabase(DB_PATH)

os.makedirs('images', exist_ok=True)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command(name='add_task')
async def add_task(ctx, *, description: str):
    task_id = db.add_task(description)
    await ctx.send(f'✅ Görev eklendi! ID: {task_id}')

@bot.command(name='delete_task')
async def delete_task(ctx, task_id: int):
    if db.delete_task(task_id):
        await ctx.send(f'🗑️ Görev {task_id} silindi!')
    else:
        await ctx.send(f'❌ Görev {task_id} bulunamadı!')

@bot.command(name='show_tasks')
async def show_tasks(ctx):
    tasks = db.get_all_tasks()
    if not tasks:
        await ctx.send('📋 Henüz görev yok!')
        return
    
    message = '📋 **Görev Listesi:**\n\n'
    for task_id, description, completed in tasks:
        status = '✅' if completed else '⏳'
        message += f'{status} **ID {task_id}:** {description}\n'
    
    await ctx.send(message)

@bot.command(name='complete_task')
async def complete_task(ctx, task_id: int):
    task = db.get_task(task_id)
    if not task:
        await ctx.send(f'❌ Görev {task_id} bulunamadı!')
        return
    
    if task[2] == 1:
        await ctx.send(f'ℹ️ Görev {task_id} zaten tamamlanmış!')
        return
    
    if db.complete_task(task_id):
        await ctx.send(f'🎉 Tebrikler! Görev {task_id} tamamlandı!\n**"{task[1]}"**')
    else:
        await ctx.send(f'❌ Bir hata oluştu!')

@bot.command(name='celebrate')
async def celebrate(ctx, task_id: int):
    task = db.get_task(task_id)
    if not task:
        await ctx.send(f'❌ Görev {task_id} bulunamadı!')
        return
    
    if task[2] != 1:
        await ctx.send(f'⚠️ Görev {task_id} henüz tamamlanmamış!')
        return
    
    img = Image.new('RGB', (800, 400), color=(255, 215, 0))
    draw = ImageDraw.Draw(img)
    
    try:
        font_large = ImageFont.truetype('arial.ttf', 60)
        font_small = ImageFont.truetype('arial.ttf', 30)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    draw.text((400, 80), '🎉 TEBRİKLER! 🎉', fill=(255, 0, 0), font=font_large, anchor='mm')
    
    wrapped_text = textwrap.fill(task[1], width=40)
    draw.text((400, 250), wrapped_text, fill=(0, 0, 0), font=font_small, anchor='mm')
    
    image_path = f'images/celebration_{task_id}.png'
    img.save(image_path)
    
    await ctx.send(file=discord.File(image_path))

bot.run(TOKEN)
