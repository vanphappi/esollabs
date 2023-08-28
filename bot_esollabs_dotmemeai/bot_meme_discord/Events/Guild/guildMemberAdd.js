const { EmbedBuilder } = require("@discordjs/builders");
const {GuildMember} = require("discord.js");

module.exports = {
  name: "guildMemberAdd",
  /**
   * @param {GuildMember} member
   */
  execute(member) {
    //Join big group
    const {user, guild} = member;
    const memberLogs = member.guild.channels.cache.get('1138310712255594509');
    const welcomeMessage = `Welcome <@${member.id}> to **dotmeme.ai**! Let's make some stuff together!`;
    
    const welcomeEmbed = new EmbedBuilder()
    .setTitle('**:partying_face: New member :partying_face: **')
    .setColor(0x4ea3f7)
    .setDescription(welcomeMessage)
    .addFields(
      { name:'Total member count:', value: `${guild.memberCount}` }
    )
    .setThumbnail('https://dotmeme.ai/static/media/iconLogo.7427747d90868a81d443.png')
    .setTimestamp();

    //Verify account
    
    
    //member.roles.add('1139030838303010906');
    memberLogs.send({embeds: [welcomeEmbed]});
    console.log(`${member.id} joined the guild.`)
  },
};