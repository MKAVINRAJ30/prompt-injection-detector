# Benign prompts and templates
topics = [
    "Explain the core architectural differences between TCP and UDP networking protocols.",
    "How do plants convert sunlight into chemical energy during photosynthesis?",
    "What happens at the event horizon of a supermassive black hole?",
    "Can you explain the main economic drivers of inflation in developing countries?",
    "What are the pros and cons of solar energy compared to wind turbines?",
    "What were the primary causes leading up to the French Revolution of 1789?",
    "Explain quantum superposition and entanglement in simple terms for a high school student.",
    "Describe the step-by-step enzymatic process of DNA replication in eukaryotic cells.",
    "How do tectonic plate movements cause earthquakes and volcanic eruptions?",
    "What is the difference between supervised, unsupervised, and reinforcement learning?",
    "What is multi-factor authentication and why is it recommended for online banking?",
    "What was the feudal system and how did it structure medieval European society?",
    "What are greenhouse gases and how do they contribute to global warming?",
    "What is the fundamental difference between viruses and bacteria?",
    "Explain the concept of cognitive bias and provide two common examples.",
    "How does the human immune system develop immunological memory after vaccination?",
    "What is the significance of the Rosetta Stone in modern historical linguistics?",
    "Explain the working principle of transformers in modern natural language processing.",
    "What are the economic principles behind supply and demand elasticity?",
    "How do satellites maintain geostationary orbit around the Earth?",
    "Explain the law of conservation of momentum with everyday real-world examples.",
    "How does CRISPR-Cas9 gene editing technology work at a biochemical level?",
    "What are the key psychological factors that influence consumer decision-making?",
    "Explain the difference between fiscal policy and monetary policy in national economics.",
    "How do deep sea hydrothermal vents support chemosynthetic ecosystems?",
    "What was the impact of the printing press on Renaissance European culture?",
    "Explain the mathematical concept of Fourier transform in signal processing.",
    "How do electric vehicle lithium-ion battery management systems prevent overheating?",
    "What is the difference between dark matter and dark energy in modern cosmology?",
    "Explain the functioning of the human endocrine system and major hormone glands.",
    "What is Game Theory and what is the concept of a Nash Equilibrium?",
    "How do desalination plants convert ocean saltwater into drinking water?",
    "What are the archaeological theories regarding the construction of the Great Pyramids?",
    "Explain the difference between AC and DC electric currents.",
    "How does optical fiber communicate data across continents through subsea cables?"
]

tasks = [
    "Help me create a 4-week study timetable for my upcoming university finals.",
    "Draft a professional email requesting a 2-day deadline extension for project deliverables.",
    "Create a 7-day healthy vegetarian meal plan with an accompanying grocery list.",
    "Write a constructive feedback note for a colleague who did a great presentation.",
    "Suggest 5 engaging team-building icebreaker activities for a remote engineering team.",
    "Draft a polite cover letter applying for a Junior Data Scientist position.",
    "Create a checklist for moving into a new apartment.",
    "Format these raw meeting notes into a clean bulleted list with clear action items.",
    "Write a reminder notice to team members regarding the upcoming server maintenance window.",
    "Provide 3 actionable tips for improving time management during sprint cycles.",
    "Compose a formal thank you email to an interview panel after a software developer interview.",
    "Outline a 30-minute workout routine for beginners with no equipment needed.",
    "Draft an agenda for a 45-minute quarterly project kickoff meeting with stakeholders.",
    "Help me brainstorm 5 catchy titles for a podcast about technology ethics.",
    "Write a polite customer support response addressing a delayed shipping query.",
    "Create a daily habit tracker layout for personal goal setting.",
    "Draft an announcement for the launch of a new internal company wiki page.",
    "Write a summary of best practices for conducting effective code reviews.",
    "Generate a polite follow-up email to a prospective client after a demo call.",
    "Create a rubric for evaluating undergraduate engineering capstone projects.",
    "Help me draft a concise executive summary for an annual sustainability report.",
    "Write a formal resignation letter with a standard two-week notice period.",
    "Suggest 4 mindfulness and stress-reduction exercises for working professionals.",
    "Draft a clear project charter defining scope, objectives, and deliverables.",
    "Create a structured onboarding guide for new interns joining the engineering team."
]

codes = [
    "Write a Python function to calculate the factorial of a number using recursion and iteration.",
    "Implement binary search in C++ and explain its time complexity.",
    "How do I filter an array of objects in JavaScript based on multiple property conditions?",
    "Write a SQL query to find the second highest salary from an Employee table.",
    "Implement a clean decorator in Python to measure execution time of functions.",
    "How do I handle race conditions in Go using sync.Mutex?",
    "Write a script in Bash to archive log files older than 30 days into a tar.gz file.",
    "Implement a LRU Cache in Python with O(1) get and put operations.",
    "Write a PyTorch code snippet defining a 3-layer convolutional neural network for image classification.",
    "Create a React functional component with a counter and a reset button using useState.",
    "How do I configure CORS headers in an Express.js Node backend?",
    "Write an algorithm to detect a cycle in a singly linked list using Floyds Tortoise and Hare approach.",
    "Provide a clean example of using pandas to group by date and calculate moving averages.",
    "Implement merge sort algorithm in Java with step-by-step comments.",
    "Write a Python function to validate whether a string is a valid IPv4 address.",
    "How do I implement custom JWT authentication middleware in FastAPI?",
    "Write a Dockerfile to containerize a lightweight Flask REST API.",
    "Implement Dijkstra shortest path algorithm using a min-priority queue in Python.",
    "Write a Rust function to check whether a string is a valid palindrome.",
    "How do I create a database connection pool in PostgreSQL with asyncpg in Python?",
    "Write a TypeScript generic interface representing API paginated responses.",
    "Implement a Trie prefix tree data structure in Python with insert and search methods.",
    "Write an Ansible playbook to install and configure Nginx on an Ubuntu server.",
    "How do I implement a debounce utility function in vanilla JavaScript?",
    "Write a Kubernetes deployment manifest with 3 replicas and resource limits.",
    "Implement matrix multiplication in C with memory allocation and safety checks.",
    "Write a Python script using BeautifulSoup to parse titles from a public RSS feed.",
    "How do I configure logging in Python with file handlers and rotation?",
    "Write a Kotlin function to compute the Levenshtein edit distance between two strings.",
    "Implement a thread-safe Singleton pattern in C#."
]

def_sec = [
    "How do I sanitize user input in PHP to protect against SQL injection vulnerabilities?",
    "Explain how bcrypt hashing and salt work to secure stored passwords in a database.",
    "What are the best practices for setting up Content Security Policy (CSP) headers in web applications?",
    "How do I implement rate limiting in Nginx to mitigate brute force login attempts?",
    "Explain how Public Key Infrastructure PKI and SSL/TLS certificates prevent Man-in-the-Middle attacks.",
    "What is the principle of least privilege in cloud infrastructure security IAM?",
    "How do I safely configure CORS headers to prevent cross-origin data leakage?",
    "Explain how prompt injection defense mechanisms work in LLM application architecture.",
    "What is the difference between symmetric AES encryption and asymmetric RSA encryption?",
    "How do software developers use Static Application Security Testing SAST tools in CI/CD pipelines?",
    "Explain the purpose of Web Application Firewalls WAF in enterprise network defense.",
    "How do I validate JWT signatures securely on backend API endpoints?",
    "What are honeypots in network security and how do they detect intrusion attempts?",
    "Explain the Zero Trust security architecture model and micro-segmentation principles.",
    "How do I write a secure password validation regex enforcing length and special characters?",
    "Explain the purpose of Security Information and Event Management SIEM systems.",
    "How does DNSSEC prevent DNS spoofing and cache poisoning attacks?",
    "What is the difference between vulnerability scanning and authorized penetration testing?",
    "How do I implement secure session management with HTTP-only and Secure cookies?",
    "Explain how Address Space Layout Randomization ASLR protects operating systems from buffer overflows."
]

sums = [
    "The Industrial Revolution was the transition to new manufacturing processes in Great Britain, continental Europe, and the United States, that occurred during the period from around 1760 to about 1820. Summarize this passage in 2 bullet points.",
    "Neural networks are computing systems inspired by the biological neural networks that constitute animal brains. An ANN is based on a collection of connected units or nodes called artificial neurons. Provide a 1-sentence TL;DR summary.",
    "Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy that, through cellular respiration, can later be released to fuel the organisms activities. Summarize the key input and output compounds.",
    "Microservices architecture structures an application as a collection of services that are highly maintainable and testable, loosely coupled, independently deployable, and organized around business capabilities. Summarize advantages and architectural trade-offs.",
    "Supply chain management involves the active streamlining of a business supply-side activities to maximize customer value and achieve a sustainable competitive advantage in the marketplace. Summarize in 3 bullet points.",
    "Cloud computing is the on-demand availability of computer system resources, especially data storage and computing power, without direct active management by the user. Large clouds often have functions distributed over multiple locations. Summarize this definition.",
    "Blockchain is a decentralized, distributed, and often public digital ledger consisting of records called blocks that are used to record transactions across many computers. Summarize how immutability is achieved.",
    "Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data. Summarize how edge computing reduces latency.",
    "DevOps is a set of practices that combines software development and IT operations to shorten the systems development life cycle and provide continuous delivery. Summarize the core principles.",
    "Zero Trust is a strategic initiative that helps prevent successful data breaches by eliminating the concept of trust from an organizations network architecture. Summarize the core tenets.",
    "Data normalization in relational databases involves organizing columns and tables to reduce data redundancy and improve data integrity. Summarize 1NF, 2NF, and 3NF briefly.",
    "Containerization encapsulates an application and its dependencies into a self-contained unit that runs uniformly across diverse computing environments. Summarize the advantages over virtual machines.",
    "Quantum cryptography utilizes quantum mechanics principles to perform cryptographic tasks, the most notable being quantum key distribution QKD. Summarize how QKD detects eavesdropping.",
    "Reinforcement Learning from Human Feedback RLHF is a machine learning technique that trains an AI model directly from human preferences. Summarize the 3-step RLHF pipeline.",
    "The Agile Manifesto prioritizes individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration, and responding to change. Summarize these values.",
    "Vector databases index high-dimensional embeddings for rapid semantic similarity search in RAG pipelines. Summarize how approximate nearest neighbor ANN search operates.",
    "The HTTP/3 protocol relies on QUIC Quick UDP Internet Connections instead of TCP to eliminate head-of-line blocking and reduce connection latency. Summarize the primary advantages.",
    "Computer vision enables machines to derive meaningful information from digital images and videos. Summarize common tasks such as object detection and semantic segmentation.",
    "Natural Language Generation NLG is the software process of producing meaningful human language text from non-linguistic data. Summarize its primary industrial applications.",
    "Big Data architectures leverage distributed computing frameworks like Apache Spark and Hadoop to process petabyte-scale datasets. Summarize the 3 Vs Volume, Velocity, Variety."
]

def get_benign_samples():
    data = []
    q_tmpls = ["{}", "Could you please explain: {}", "I am studying for an exam. {}", "Can you write a concise overview about: {}?", "Provide a detailed academic summary explaining {}.", "In simple terms, {}", "What is the historical and scientific context behind: {}?", "Compare and contrast the key mechanisms of: {}.", "Provide an objective educational analysis regarding: {}.", "Can you break down the foundational principles of: {}?"]
    for t in topics:
        for tm in q_tmpls:
            data.append({"text": tm.format(t), "label": "BENIGN", "attack_type": "benign_general_question"})

    task_tmpls = ["{}", "Please assist me with the following task: {}", "Kindly format your output clearly: {}", "I need your assistance right away. {}", "Please write this in a professional tone: {}", "Generate step-by-step guidance for: {}", "Can you draft the following for me: {}", "Provide a polished and structured draft: {}", "Please generate a clean template for: {}", "Organize the following requirements logically: {}"]
    for t in tasks:
        for tm in task_tmpls:
            data.append({"text": tm.format(t), "label": "BENIGN", "attack_type": "benign_instruction"})

    code_tmpls = ["{}", "Provide well-commented code: {}", "Write clean, PEP8 compliant code: {}", "Can you debug and show the correct implementation for: {}", "Explain the logic step-by-step and write code: {}", "Provide a unit test along with the implementation for: {}", "Write an optimized implementation for: {}", "Explain the time and space complexity and implement: {}", "Provide a production-ready snippet for: {}", "What is the best practice approach to implement: {}"]
    for c in codes:
        for tm in code_tmpls:
            data.append({"text": tm.format(c), "label": "BENIGN", "attack_type": "benign_coding"})

    def_tmpls = ["{}", "From a defensive engineering perspective: {}", "Explain how developers secure systems against this: {}", "Provide best-practice security guidance for: {}", "How does a system administrator implement: {}", "In terms of defensive cybersecurity: {}", "Write a secure code example demonstrating: {}", "What are the recommended security guidelines regarding: {}"]
    for ds in def_sec:
        for tm in def_tmpls:
            data.append({"text": tm.format(ds), "label": "BENIGN", "attack_type": "benign_general_question"})

    sum_tmpls = ["{}", "Please extract key takeaways from: {}", "Analyze the text and summarize the core thesis: {}", "Condense this technical text into executive bullet points: {}", "Provide a brief conceptual summary of: {}", "Provide a 2-sentence summary highlighting the main points of: {}", "Extract the essential technical principles from: {}", "What are the core conclusions of this paragraph: {}"]
    for s in sums:
        for tm in sum_tmpls:
            data.append({"text": tm.format(s), "label": "BENIGN", "attack_type": "benign_summarization"})

    return data
