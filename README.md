## Testing
### Outline of elements to test
⋅⋅*If question number matches correct question
..*If user gets question right, count goes up
..*If incorrect, guess_number count goes up
..*On second incorrect guess, count doesnt go up
..*current_question count can't be more than length of questions
..*incorrect answers don't increase correct answer count.
..*low score count true if score < len/2, false if score >= len/2