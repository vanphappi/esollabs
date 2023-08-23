const { Telegraf } = require('telegraf');
const { message } = require('telegraf/filters');

const bot = new Telegraf('6533497382:AAHgC61oPsAuMVKwcbVLDDjq3SLBxkcAikg');

function get_link_verify(id_user){
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
      fetch("https://dns-stag.dotmeme.ai/v1/api/user/profile?owner=0x5d12ffaf4ab3d70b5c3941dd6a29fc6fc4415eb4", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));   

    return;
}

bot.start((ctx) => {
    var id_user = ctx.message.from.id
    ctx.reply("Hi there! Please verify you own the dns of dotmeme.ai; Click the Verify button to verify!!!", {
        
        reply_markup: {
            inline_keyboard: [
                /* Inline buttons. 2 side-by-side */
                //[ { text: "Button 1", callback_data: "btn-1" }, { text: "Button 2", callback_data: "btn-2" } ],

                /* One button */
                //[ { text: "Next", callback_data: "next" } ],
                
                /* Also, we can have URL buttons. */
                [ { text: "Verify", url: "dotmeme.ai" } ]
            ]
        }
    });
});
bot.command("verify", (ctx) => {
    var id_user = ctx.message.from.id
    var id = get_link_verify(id_user)
    ctx.reply("Hi there! Please verify you own the dns of dotmeme.ai; Click the Verify button to verify!!!", {
        reply_markup: {
            inline_keyboard: [
                /* Inline buttons. 2 side-by-side */
                //[ { text: "Button 1", callback_data: "btn-1" }, { text: "Button 2", callback_data: "btn-2" } ],

                /* One button */
                //[ { text: "Next", callback_data: "next" } ],
                
                /* Also, we can have URL buttons. */
                [ { text: "Verify", url: "dotmeme.ai" } ]
            ]
        }
    });
});
bot.launch();
