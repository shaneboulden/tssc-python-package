import os

import pytest
from testfixtures import TempDirectory
import yaml

from tssc import TSSCFactory
from tssc.step_implementers.push_artifacts import Maven

from test_utils import *


# Example CLI command for push to artifactory
#mvn deploy:deploy-file \
#-DgroupId=org.acme \
#-DartifactId=rest-json-quickstart \
#-Dversion=1.0.2-ce5f284-SNAPSHOT \
#-Dpackaging=jar \
#-Dfile=target/tssc-reference-app-quarkus-rest-jsont-1.0-SNAPSHOT.jar \
#-DrepositoryId=snapshots \
#-Durl=http://artifactory.apps.tssc.rht-set.com/artifactory/libs-snapshot/

def test_push_artifact_with_artifact_id_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')
        pom_file_path = os.path.join(temp_dir.path, 'pom.xml')

        generate_metadata_config = {
            'tssc-config': {
                'generate-metadata': {
                    'implementer': 'Maven'
                 }
            }
        }
        run_step_generate_metadata_for_tests(temp_dir, generate_metadata_config, runtime_args={'pom-file': str(pom_file_path)})

        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'generate-metadata': {'app-version': '42.1'}, 'push-artifacts': {'version':'42.1'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

"""
def test_push_artifact_with_file_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_file_path_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_group_id_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_packaging_invalid():# TODO: Test for JAR/WAR/EAR
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_packaging_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_repository_id_invalid():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_repository_id_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_repository_url_invalid():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_repository_url_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_version_malformed():# SNAPSHOT check
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
    <version>42.1-SNAPSHOT</version>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)

def test_push_artifact_with_version_missing():
    with TempDirectory() as temp_dir:
        temp_dir.write('pom.xml',b'''<project>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>my-app</artifactId>
    <groupId>com.mycompany.app</groupId>
</project>''')  
        config = {
            'tssc-config': {    
                'push-artifacts': {
                    'implementer': 'Maven',
                    'config': {
                        'packaging': 'jar',
                        'repository': {
                            'id': 'id',
                            'url': 'url'
                        }
                    }
                }
            }
        }
        expected_step_results = {'tssc-results': {'push-artifacts': {'version': 'version'}}}

        run_step_test_with_result_validation(temp_dir, 'push-artifacts', config, expected_step_results)
"""

