---
description: Administer the PHQ-9 depression screening questionnaire one question at a time. Use when the user asks to take a PHQ-9, depression screening, mental health check, or mood assessment.
---

# PHQ-9 Depression Screening

**Goal**: Collect all 9 PHQ-9 responses, score them, and interpret the result.

## The 9 Questions

Ask one question per turn. Each measures frequency over the **past two weeks**:

0. Not at all  
1. Several days  
2. More than half the days  
3. Nearly every day

1. Little interest or pleasure in doing things
2. Feeling down, depressed, or hopeless
3. Trouble falling/staying asleep, or sleeping too much
4. Feeling tired or having little energy
5. Poor appetite or overeating
6. Feeling bad about yourself — or that you are a failure or have let yourself or your family down
7. Trouble concentrating on things, such as reading the newspaper or watching television
8. Moving or speaking so slowly that other people could have noticed. Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual
9. Thoughts that you would be better off dead, or of hurting yourself in some way

## Steps

1. **Track state across turns**. Maintain a list of which questions have been answered and their scores.

2. **Ask the next unanswered question**. Present it with the 0-3 scale. Wait for the user's response before continuing.

3. **Validate the response**. Accept 0-3 as valid scores. If invalid, re-ask the same question.

4. **Loop until all 9 answered**. After each valid response, check: are all 9 questions done? If not, return to step 2 on the next turn.

5. **Score and interpret**. Sum all 9 scores:
   - **0-4**: Minimal depression
   - **5-9**: Mild depression
   - **10-14**: Moderate depression
   - **15-19**: Moderately severe depression
   - **20-27**: Severe depression

   Present the total score, severity category, and standard clinical guidance: PHQ-9 ≥10 suggests clinical depression and warrants professional evaluation.

**Completion criterion**: All 9 questions answered with valid scores (0-3), total calculated, and interpretation presented.

## Notes

- This is a **screening tool**, not a diagnosis. Always recommend professional consultation for scores ≥10 or any suicidal ideation (question 9 > 0).
- If the user discloses active suicidal intent at any point, prioritize crisis resources over completing the questionnaire.
