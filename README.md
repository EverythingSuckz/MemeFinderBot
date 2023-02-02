# Find Your Meme Bot
Meme Finder Telegram bot powered by [findthatmeme.com](https://findthatmeme.com)

## Demo
  Available as [@FindThatMemeBot](https://telegram.dog/FindThatMemeBot)

## Hosting
### Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FEverythingSuckz%2FMemeFinderBot&env=BOT_TOKEN&envDescription=Your%20API%20token%20for%20your%20bot.&envLink=https%3A%2F%2Ftelegram.dog%2FBotFather&project-name=meme-finder-bot-clone&repository-name=meme-finder-bot-clone&demo-title=Meme%20FInder%20Bot&demo-description=A%20telegram%20bot%20to%20find%20memes%20easily%20via%20inline.&demo-url=https%3A%2F%2Ftelegram.dog%2FFindThatMemeBot&demo-image=https%3A%2F%2Fembed.pixiv.net%2Fartwork.php%3Fillust_id%3D97404887)

> **Note**: After deployment, Goto the `/updateWebhooks?token=\<your bot token\>`  path of your deployed app url to setup webhooks.
> An example will be https://meme-search-bot.vercel.app/updateWebhooks?token=your-bot-token

### Self Hosting

```bash
python -m bot
```

## Credits
- [aiogram](https://aiogram.dev/)
- [tg-serverless](https://github.com/illvart/tg-serverless)
- [fastapi-aiogram](https://github.com/malikovss/fastapi-aiogram)