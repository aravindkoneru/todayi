import click

from .cli_options import *


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@report
def cli(report: bool):
    if report:
        raise NotImplemented("TODO: Implement reporting")
        # TODO: generate and show report
    else:
        raise NotImplemented("TODO: Implement adding tasks to entries")
