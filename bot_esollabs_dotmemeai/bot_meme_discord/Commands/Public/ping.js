const {
    SlashCommandBuilder,
    CommandInteraction,
    PermissionFlagsBits,
  } = require("discord.js");

  
  module.exports = {
    name: "Interaction",
    data: new SlashCommandBuilder()
      .setName("verify")
      .setDescription("Verify")
      .setDefaultMemberPermissions(PermissionFlagsBits.SendMessages),
    /**
     *
     * @param {CommandInteraction} interaction
     */

  
    execute(interaction,member) {
      
      interaction.reply({content: "Pong", ephermal: true});
    },

  };