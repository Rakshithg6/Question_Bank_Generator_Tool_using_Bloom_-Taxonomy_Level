prompt_template = """
        Generate a question bank using Bloom's Taxonomy from the provided content.
 
        You need to create 20 questions for each level of Bloom's Taxonomy based on the specified action verbs. Each question should clearly reflect its targeted taxonomy level and adhere to the following specifications.
 
        *Knowledge-Based Questions: Use verbs such as **define, **memorize, **repeat, **copy, **identify, **state, **list, **quote, or **find*.
        *Comprehension-Based Questions: Employ verbs like **summarize, **compare, **describe, **explain, **discuss, **recognize, **report, **translate, and **categorize*.
        *Application-Based Questions: Implement verbs such as **determine, **present, **examine, **implement, **solve, **use, **demonstrate, **interpret, and **reenact*.
        *Analysis-Based Questions: Include verbs such as **organize, **compare, **contrast, **experiment, **test, **question, **connect, **deduce, and **link*.
        *Synthesis-Based Questions: Use verbs like **design, **compose, **construct, **develop, **formulate, **build, **write, or **simulate*.
        *Evaluation-Based Questions: Apply verbs such as **argue, **defend, **judge, **support, **value, **weigh, **reflect, **review, and **grade*.
 
        # Steps
 
        1. Read the provided content {context}.
        2. For each taxonomy level, generate four unique questions employing the related verbs.
        3. Ensure that each question incorporates at least one action verb, which should be in bold.
        4. After composing the question, append its taxonomy level in square brackets at the end.
        5. Each question must conclude with a period.
 
        # Output Format
 
        Produce questions in the following format: "[Question Text] [Taxonomy Level in square brackets with action verbs in *bold*]."
 
        # Examples
 
        ### Knowledge-Based Questions Example:
        What is the primary function of the *heart*? [Knowledge]
        *Identify* the components of the *solar* system. [Knowledge]
 
        ### Comprehension-Based Questions Example:
        *Explain* how photosynthesis occurs in *plants*. [Comprehension]
        *Describe* the *process* of cellular respiration. [Comprehension]
 
        ### Application-Based Questions Example:
        *Solve* for the variable *x* in the equation 2x + 3 = 7. [Application]
        *Demonstrate* how to *prepare* a simple salad. [Application]
 
        ### Analysis-Based Questions Example:
        *Contrast* the *nervous* system with the *endocrine* system. [Analysis]
        *Test* the *effects* of sunlight on plant growth. [Analysis]
 
        ### Synthesis-Based Questions Example:
        *Design* an *experiment* to test water purity. [Synthesis]
        *Compose* a *short* story based on the given theme. [Synthesis]
 
        ### Evaluation-Based Questions Example:
        *Defend* the *importance* of renewable energy. [Evaluation]
        *Judge* the *effectiveness* of the new law on pollution control. [Evaluation]
 
        (Note: For real examples, ensure that questions align with the specific content and context provided.)
    """