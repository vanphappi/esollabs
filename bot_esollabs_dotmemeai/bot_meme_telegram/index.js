const { Telegraf } = require('telegraf');
const { message } = require('telegraf/filters');

const bot = new Telegraf('6533497382:AAHgC61oPsAuMVKwcbVLDDjq3SLBxkcAikg');

function get_link_verify(id_user){
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };

    var link_verify = fetch("http://62.72.44.94:8080/dotmeme.ai/id="+id_user)
        .then(response => {
            if (response.ok) {
                return response.text();
            } else {
                throw new Error('error');
            }
        });
    return link_verify
}

bot.start((ctx) => {
    var id_user = ctx.message.from.id
    get_link_verify(id_user).then(function(result){
        ctx.reply("Hi there! Please verify you own the dns of dotmeme.ai; Click the Verify button to verify!!!", {
            reply_markup: {
                inline_keyboard: [
                    /* Inline buttons. 2 side-by-side */
                    //[ { text: "Button 1", callback_data: "btn-1" }, { text: "Button 2", callback_data: "btn-2" } ],
    
                    /* One button */
                    //[ { text: "Next", callback_data: "next" } ],
                    
                    /* Also, we can have URL buttons. */
                    [ { text: "Verify", url: result } ]
                ]
            }
        });
    })
});
bot.command("verify", (ctx) => {
    var id_user = ctx.message.from.id
    get_link_verify(id_user).then(function(result){
        ctx.reply("Hi there! Please verify you own the dns of dotmeme.ai; Click the Verify button to verify!!!", {
            reply_markup: {
                inline_keyboard: [
                    /* Inline buttons. 2 side-by-side */
                    //[ { text: "Button 1", callback_data: "btn-1" }, { text: "Button 2", callback_data: "btn-2" } ],
    
                    /* One button */
                    //[ { text: "Next", callback_data: "next" } ],
                    
                    /* Also, we can have URL buttons. */
                    [ { text: "Verify", url: result } ]
                ]
            }
        });
    })
});
bot.launch();
