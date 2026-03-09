from mcp.server.fastmcp import FastMCP

mcp = FastMCP("simple-public-echo")


@mcp.tool()
def ping(message: str) -> str:
    return f"pong:{message}"


@mcp.resource(
    "memo://welcome",
    name="welcome-note",
    title="Welcome Note",
    description="Static markdown resource for public MCP smoke testing.",
    mime_type="text/markdown",
)
def welcome_note() -> str:
    return """# Public MCP smoke

This resource exists so Dock0 can list and open a simple static resource.
Revision marker: personal account public smoke 20260309.
"""


@mcp.resource(
    "memo://samples/config",
    name="sample-config",
    title="Sample Config",
    description="Static JSON resource with a few smoke-test fields.",
    mime_type="application/json",
)
def sample_config() -> dict[str, object]:
    return {
        "server": "simple-public-echo",
        "mode": "public-smoke",
        "account": "Miridar",
        "capabilities": ["tools", "resources", "prompts"],
    }


@mcp.resource(
    "memo://profiles/{profile}",
    name="profile-card",
    title="Profile Card",
    description="Template resource that renders a tiny profile by name.",
    mime_type="text/plain",
)
def profile_card(profile: str) -> str:
    return (
        f"Profile: {profile}\n"
        "Visibility: public\n"
        "Purpose: smoke-test templated resource discovery"
    )


@mcp.prompt(
    name="summarize-smoke-context",
    title="Summarize Smoke Context",
    description="Simple prompt with an optional goal argument.",
)
def summarize_smoke_context(goal: str = "Confirm personal public MCP listing") -> str:
    return (
        "You are validating a public MCP deployment under the Miridar account. "
        f"Summarize the current goal in one short paragraph: {goal}."
    )


@mcp.prompt(
    name="review-profile",
    title="Review Profile",
    description="Prompt that points the model at a templated profile resource URI.",
)
def review_profile(profile: str) -> str:
    return (
        f"Review the resource at memo://profiles/{profile} "
        "and write two bullet points about what it contains."
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
