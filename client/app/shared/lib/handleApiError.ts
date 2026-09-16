import {FetchError} from "ofetch"

export function getErrorMessage(err : unknown , fallback = "Internal Server Error"):string{
    if (err instanceof FetchError){
        return err.data?.detail ?? fallback
    }

    if(err instanceof  Error){
        return err.message
    }   

    return fallback
}