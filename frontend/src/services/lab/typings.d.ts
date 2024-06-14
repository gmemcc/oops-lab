declare namespace API {
  type deleteApiReportsIdDeleteParams = {
    id: number;
  };

  type getByIdApiReportsIdGetParams = {
    id: number;
  };

  type HTTPValidationError = {
    /** Detail */
    detail?: ValidationError[];
  };

  type PageReportModel_ = {
    /** Data */
    data: ReportModel[];
    /** Success */
    success: boolean;
    /** Total */
    total: number;
  };

  type queryApiReportsQueryPostParams = {
    reporter?: string | null;
    report_time?: string | null;
  };

  type ReportModel = {
    /** Id */
    id: number | null;
    /** Reporter */
    reporter: string | null;
    /** Reporttime */
    reportTime: string | null;
    /** Workcontent */
    workContent: string | null;
    /** Concernedincs */
    concernedIncs: string | null;
  };

  type updateApiReportsIdPutParams = {
    id: number;
  };

  type ValidationError = {
    /** Location */
    loc: (string | number)[];
    /** Message */
    msg: string;
    /** Error Type */
    type: string;
  };
}
