/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mlindhol.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mlindhol <mlindhol@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/23 14:32:37 by mlindhol          #+#    #+#             */
/*   Updated: 2020/03/23 14:32:37 by mlindhol         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>

int     hv_necklace(char *s1, char *s2)
{  
    size_t      len2;
    size_t      i;
    size_t      j;

    len2 = strlen(s2);
    i = 0;
    j = 0;

    if (s1 == s2)
        return (1);
    if (strlen(s1) != len2)
        return (0);
    if (!strchr(s2, s1[0]))
        return (0);
    while (j < len2)
    {
        while (s1[i] && s2[j] && s1[i] == s2[j])
        {
            if (s1[i + 1] && s2[j + 1] && s1[i + 1] != s2[j + 1])
                break;
            ++i;
            ++j;
            if (s1[i] && !s2[j])
            {
                j = 0;
                if (s1[i] != s2[j])
                    return (0);
            }
            if (!s1[i])
                return (1);
        }
        i = 0;
        ++j;
    }
    return (0);
}
