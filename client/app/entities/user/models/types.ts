export interface IUser {
  id: string;
  full_name: string;
  username: string | null;
  telegram_id: number;
  registered_at: string;
}

export interface ISessions {
  id: string;
  device_id: string;
  os_name: string | null;
  os_version: string | null;
  browser_name: string | null;
  browser_version: string | null;
  ip_address: string | null;
  last_seen_at: string;
  created_at: string;
  is_current: boolean;
}

export interface ResponseSessions {
  sessions: ISessions[];
}

export interface ResponseRemoveSession{
  success: boolean , 
  message : string
}
