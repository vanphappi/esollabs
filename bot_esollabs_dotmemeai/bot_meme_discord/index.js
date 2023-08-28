const {Client, GatewayIntentBits,ActionRowBuilder, Partials, Collection, ButtonBuilder,ButtonStyle} = require('discord.js');

const {Guilds, GuildMembers, GuildMessages} = GatewayIntentBits;

const {User, Message, GuildMember, ThreadMember, Channel} = Partials;

const { promisify } = require('util')

const client = new Client({
    intents:[Guilds, GuildMembers, GuildMessages],
    partials:[User, Message, GuildMember, ThreadMember],
});

const {loadEvents} = require("./Handlers/eventHandler");
const {loadCommands} = require("./Handlers/commandHandler");

const roles = [{
  id: '1139030838303010906',
  label: 'Verify'
}]

client.once('ready',async (c) =>{
  try{
    const channel = await client.channels.cache.get('1145636991447347292')
    if(!channel) return;

    const row = new ActionRowBuilder();

    roles.forEach((role) => {
      row.components.push(
        new ButtonBuilder()
          .setCustomId(role.id)
          .setLabel(role.label)
          .setStyle(ButtonStyle.Primary)
      );
    });


    await channel.send({
      content: 'Click the verify button to get the verification link',
      components: [row],
    });
    //process.exit();


  }catch(error){
    console.log(error)
  }
   
});


client.on('interactionCreate',async (interaction)=>{
  try {
    if (!interaction.isButton()) return;
    await interaction.deferReply({ ephemeral: true });

    const role = interaction.guild.roles.cache.get(interaction.customId);
   

    const hasRole = interaction.member.roles.cache.has(role.id);

    const id_user = interaction.member.id;

    //Verify
    get_link_verify(id_user).then( async function(result){ 
      await interaction.member.send(`Your authentication link is: ${result}. The link is valid for 3 minutes, please click the verify button to generate a new verification link if the link is expired or broken`)
    })


    var check_user_verify =  setInterval(()=>{
      check_has_verify(id_user).then( async function(result){ 
        if(result != '0'){
          await interaction.member.roles.add(role);
          await interaction.member.send(`You have successfully verified`);
          clearInterval(check_user_verify)
        }
      })
    }, 1000);

  } catch (error) {
    console.log(error);
  }
});

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


function check_has_verify(id_user){
  var requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };

  var verify = fetch("http://62.72.44.94:8080/dotmeme.ai/user_verify_discord/userid="+id_user)
    .then(response => {
    if (response.ok) {
      return response.text();
    } else {
      throw new Error('error');
    }
  });
  return verify;
}


client.commands = new Collection();

client.config = require('./config.json');

client
  .login(client.config.token)
  .then(() => {
    loadCommands(client);
    loadEvents(client);
  })
  .catch((err) => console.log(err));


