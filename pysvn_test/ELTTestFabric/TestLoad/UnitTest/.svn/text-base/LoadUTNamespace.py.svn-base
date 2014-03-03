from VerifyCTRLData import VerifyCTRLData
from VerifyDBData import VerifyDBData
from SampleTC3 import SampleTC3

test_case_namespace = {
						1 : [VerifyCTRLData, "Verify CTRL files for Integrity", {"act_res_dir"  : "actual_results", "exp_res_dir" : "expected_results", "test_case_no" : "99" }  ],
                        2 : [VerifyDBData, "Test Case 2", {"test_case_no" : "71",  "table" :
                                    "etl_process_status",   "pkey" :
                                    "BATCH_SK,PROCESS_SK",    "non_pkey" :
                                    "MIN_BATCH_ID,PROCESS_NAME",    "where" :
                                    "PROCESS_NAME,=,'wf_SFF_BRANCHED_QUESTIONS'",
                                    "mode" : "C",   "run" : "A",} ],
                        3 : [SampleTC3, "Test Case 3", {"3" : "3"}],
						}
