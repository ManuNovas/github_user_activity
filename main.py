from sys import argv

from src.adapters.builders import GithubBuilderAdapter
from src.adapters.input import GithubInputAdapter
from src.adapters.output import GithubOutputAdapter
from src.application.use_cases import GithubUseCases


output = GithubOutputAdapter()
builder = GithubBuilderAdapter()
use_cases = GithubUseCases(output, builder)
input = GithubInputAdapter(use_cases)
input.main(argv)
