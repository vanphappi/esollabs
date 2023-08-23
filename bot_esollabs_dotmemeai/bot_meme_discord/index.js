// const {Client, GatewayIntentBits, Partials, Collection} = require('discord.js');

// const {Guilds, GuildMembers, GuildMessages} = GatewayIntentBits;

// const {User, Message, GuildMember, ThreadMember, Channel} = Partials;

// const client = new Client({
//     intents:[Guilds, GuildMembers, GuildMessages],
//     partials:[User, Message, GuildMember, ThreadMember],
// });

// const {loadEvents} = require("./Handlers/eventHandler");
// const {loadCommands} = require("./Handlers/commandHandler");

// client.once('ready',() =>{
//     console.log('Ready!');
// });

// client.commands = new Collection();

// client.config = require('./config.json');

// client
//   .login(client.config.token)
//   .then(() => {
//     loadCommands(client);
//     loadEvents(client);
//   })
//   .catch((err) => console.log(err));



var formdata = new FormData();
formdata.append("address", "1");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("http://127.0.0.1:5000/verify", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));