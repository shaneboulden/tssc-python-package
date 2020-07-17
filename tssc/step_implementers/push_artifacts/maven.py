"""
Step Implementer for the push-artifacts step for Maven.
"""

from tssc import TSSCFactory
from tssc import StepImplementer
from tssc import DefaultSteps

DEFAULT_ARGS = {}

class Maven(StepImplementer):
    """
    StepImplementer for the push-artifacts step for Maven.
    """

    def __init__(self, config, results_dir, results_file_name):
        super().__init__(config, results_dir, results_file_name, DEFAULT_ARGS)

    @classmethod
    def step_name(cls):
        return DefaultSteps.PUSH_ARTIFACTS

    def _validate_step_config(self, step_config):
        """
        Function for implementers to override to do custom step config validation.

        Parameters
        ----------
        step_config : dict
            Step configuration to validate.
        """

    def _run_step(self, runtime_step_config):

        """                  
        # Example CLI command to push artifacts:
        mvn deploy:deploy-file \
        -DgroupId=org.acme \
        -DartifactId=rest-json-quickstart \
        -Dversion=1.0.2-ce5f284-SNAPSHOT \
        -Dpackaging=jar \
        -Dfile=target/tssc-reference-app-quarkus-rest-jsont-1.0-SNAPSHOT.jar \
        -DrepositoryId=snapshots \
        -Durl=http://artifactory.apps.tssc.rht-set.com/artifactory/libs-snapshot/

        # Consider the following:
        ## settings.xml
        ## groupId      
        ## artifactId   
        ## version      
        ## packaging    
        ## file         
        ## repository   
        ## url          
        """                  
        
        # Getting the semantic version information from the hopefully previously run generate-metadata step
        version = "latest"
        try:
            version = self.get_step_results('generate-metadata')['app-version']
        except KeyError:
            print('No version found in metadata. Using latest')

        results = {
                'version' : version
        }

        return results

# register step implementer
TSSCFactory.register_step_implementer(Maven)
