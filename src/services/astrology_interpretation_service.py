"""Service for generating personalized Vedic astrology interpretations using LLM."""

from typing import Any, Dict

from src.services.llm_service import llm_service


class AstrologyInterpretationService:
    """Generates personalized astrology readings using LLM based on planetary positions."""

    ASTROLOGY_SYSTEM_PROMPT = """You are an expert Vedic astrologer with deep knowledge of planetary influences, personality analysis, and future prediction. 

You interpret planetary positions and zodiac signs to provide personalized, insightful readings.

When generating readings:
- Use simple, clear, human-friendly language
- Interpret meaning based on astrology principles
- Keep response structured and insightful
- Avoid generic statements — be specific and personalized
- Use the exact format requested
- Speak in a mystical and wise tone, like an ancient astrologer
- Reference the specific planets and signs provided
- Make connections between planetary placements
- Provide actionable insights"""

    ASTROLOGY_GENERATION_PROMPT = """You are a renowned Vedic astrologer. Based on the following birthart and planetary positions, generate a comprehensive, personalized astrology reading.

**CLIENT INFORMATION:**
Name: {name}
Date of Birth: {dob}
Time of Birth: {time}
Location: {location}

**PLANETARY POSITIONS:**
{planet_data}

**ZODIAC SIGN MEANINGS:**
- Aries (♈): Leadership, courage, action, passion
- Taurus (♉): Stability, loyalty, material focus, sensuality
- Gemini (♊): Communication, curiosity, adaptability, intellect
- Cancer (♋): Emotion, intuition, family, nurturing
- Leo (♌): Creativity, confidence, authority, generosity
- Virgo (♍): Analysis, perfection, service, health
- Libra (♎): Balance, harmony, relationships, justice
- Scorpio (♏): Intensity, secrecy, transformation, power
- Sagittarius (♐): Expansion, wisdom, adventure, philosophy
- Capricorn (♑): Discipline, responsibility, ambition, structure
- Aquarius (♒): Innovation, humanitarianism, independence, logic
- Pisces (♓): Compassion, spirituality, imagination, escapism

**PLANET MEANINGS (in brief):**
- Sun: Core identity, ego, life purpose, vitality
- Moon: Emotions, mind, comfort, inner self
- Mars: Action, passion, aggression, sexuality
- Mercury: Communication, intellect, learning
- Venus: Love, values, pleasure, finances
- Jupiter: Luck, expansion, wisdom, spirituality
- Saturn: Discipline, challenges, karma, maturity
- Rahu: Desires, ambitions, north node influence
- Ketu: Spirituality, detachment, south node influence

---

Generate a reading in the following format:

**🔮 PERSONALITY TRAITS:**
[Based on Sun and Moon placement, describe the core personality, emotional nature, and how they present themselves to the world. Be specific about their Sun sign qualities modulated by Moon sign.]

**🌟 STRENGTHS:**
[Based on beneficial planetary placements, list 4-5 specific strengths. Explain how each strength manifests in their life.]

**⚠️ WEAKNESSES & CHALLENGES:**
[Based on challenging aspects and placements, describe 4-5 areas where they might struggle. Provide context from astrology.]

**💼 CAREER & LIFE PATH INSIGHTS:**
[Based on Mercury, Jupiter, Saturn, and 10th house ruler (if visible in planets), suggest suitable careers and life paths. Mention obstacles and how to overcome them.]

**🔮 FUTURE PREDICTIONS:**

*Short Term (Next 6-12 months):*
[Based on current planetary positions, mention upcoming opportunities, challenges, or transitions. Reference specific planets.]

*Long Term (2-5 years):*
[Describe the broader trajectory and transformation based on planetary cycles and positions.]

**🧭 GUIDANCE & REMEDIES:**
[Based on their birth chart, offer:
1. Life advice aligned with their planetary nature
2. Best days/times for important decisions
3. Practices or mantras if appropriate
4. How to work with their cosmic energy]

---

Generate a personalized, deeply insightful reading. Every point should reference their actual planetary positions. Be mystical yet practical."""

    def format_planet_data(self, planets: Dict[str, Any]) -> str:
        """Format planetary positions into readable text for LLM."""
        planet_lines = []
        for planet_name, data in planets.items():
            line = (
                f"{data['emoji']} {planet_name}: {data['degrees']:.2f}° in "
                f"{data['sign_name']} ({data['degree_in_sign']:.2f}° {data['sign_name']})"
            )
            planet_lines.append(line)
        return "\n".join(planet_lines)

    def generate_reading(
        self, name: str, dob: str, time: str, location: str, planets: Dict[str, Any]
    ) -> str:
        """Generate a personalized astrology reading using LLM.
        
        Args:
            name: Person's name
            dob: Date of birth (YYYY-MM-DD)
            time: Birth time (HH:MM)
            location: Birth location
            planets: Dictionary of planetary positions from astrology_service
            
        Returns:
            Personalized astrology reading as a string
        """
        planet_data = self.format_planet_data(planets)

        prompt = self.ASTROLOGY_GENERATION_PROMPT.format(
            name=name, dob=dob, time=time, location=location, planet_data=planet_data
        )

        try:
            reading = llm_service.query_llama(
                prompt, context="", system_prompt=self.ASTROLOGY_SYSTEM_PROMPT
            )
            return reading
        except Exception as e:
            return f"Error generating astrology reading: {str(e)}"


astrology_interpretation_service = AstrologyInterpretationService()
