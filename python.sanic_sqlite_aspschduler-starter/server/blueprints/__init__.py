'''
Should define in format:

{

  bp_name: (blueprint, blueprint_options)

{
'''
from blueprints.home import home_bp

blueprints = {
  home_bp.name: (home_bp, dict())
}
