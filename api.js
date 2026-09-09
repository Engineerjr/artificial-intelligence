import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "<REDACTED>" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();